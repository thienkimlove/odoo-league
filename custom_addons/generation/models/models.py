# -*- coding: utf-8 -*-
from logging import log

from odoo import models, fields, api
from addons.http_routing.models.ir_http import slugify



class TimeModel(models.AbstractModel):
    _name = 'generation.time'    
    name = fields.Char('Name')
    active = fields.Boolean('Is Active?', default=True)    
    slug = fields.Char("Slug", compute='_compute_slug')

    @api.depends('name')
    def _compute_slug(self):
        for r in self:
            r.slug = slugify(r.name)
                 

class Stadium(models.Model):
    _name = 'generation.stadium'
    _description = 'Stadium'
    _inherit = ['generation.time']
    


class Season(models.Model):
    _name = 'generation.season'
    _description = 'Season'
    _inherit = ['generation.time']

class Position(models.Model):
    _name = 'generation.position'
    _description = 'Position'
    _inherit = ['generation.time']

class League(models.Model):
    _name = 'generation.league'
    _description = 'League'
    _inherit = ['generation.time']
    
    season_id = fields.Many2one('generation.season', 'Season')

class Club(models.Model):
    _name = 'generation.club'
    _description = 'Club'
    _inherit = ['generation.time']

    image = fields.Binary('Image')
    stadium_id = fields.Many2one('generation.stadium', 'Stadium')

class Player(models.Model):
    _name = 'generation.player'
    _description = 'Player'
    _inherit = ['generation.time']
    
    dob = fields.Date('DOB')
    country_id = fields.Many2one('res.country', 'Country')
    height = fields.Integer('Height')
    weight = fields.Integer('Weight')
    position_id = fields.Many2one('generation.position', 'Position')
    club_id = fields.Many2one('generation.club', 'Club')
    image = fields.Binary('Image')
    history_ids = fields.Many2many('generation.club', string='History', readonly=True)


    @api.model
    def create(self, vals):
        vals['history_ids'] = [(6, 0, [vals.get('club_id')])]
        record = super(Player, self).create(vals)
        return record

    @api.multi
    def write(self, vals):
        vals['history_ids'] = [(4, vals.get('club_id'), 0)]
        super(Player, self).write(vals)
        return True


class Referee(models.Model):
    _name = 'generation.referee'
    _description = 'Referee'
    _inherit = ['generation.time']
    
    dob = fields.Date('DOB')
    country_id = fields.Many2one('res.country', 'Country')
    height = fields.Integer('Height')
    weight = fields.Integer('Weight')
    image = fields.Binary('Image')

class Coach(models.Model):
    _name = 'generation.coach'
    _description = 'Coach'
    _inherit = ['generation.time']
    
    dob = fields.Date('DOB')
    country_id = fields.Many2one('res.country', 'Country')
    height = fields.Integer('Height')
    weight = fields.Integer('Weight')
    image = fields.Binary('Image')
    club_id = fields.Many2one('generation.club', 'Club')
    
class Match(models.Model):
    _name = 'generation.match'
    _description = 'Match'
    _inherit = ['generation.time']

    name = fields.Char('Name', readonly=1, compute='_compute_match_name')

    home_club_id = fields.Many2one('generation.club', 'Home Club',)
    away_club_id = fields.Many2one('generation.club', 'Away Club')

    start_home_player_ids = fields.Many2many('generation.player', string='Home Team Player Start Match', domain="[('club_id','=',home_club_id)]")
    start_away_player_ids = fields.Many2many('generation.player', string='Away Team Player Start Match',  domain="[('club_id','=',away_club_id)]")
    referee = fields.Many2one('generation.referee', 'Referee')
    start_time = fields.Datetime('Start Time')
    end_time = fields.Datetime('End Time')
    league_id = fields.Many2one('generation.league', 'League')
    stadium_id = fields.Many2one('generation.stadium', 'Stadium')
    home_score = fields.Integer('Home Store')
    away_score = fields.Integer('Away Store')
    match_detail_ids = fields.One2many(
        'generation.match_detail',
        'match_id',
        'Details')

    @api.depends('home_club_id.name', 'away_club_id.name', 'start_time')
    def _compute_match_name(self):
        for r in self:
            r.name = '{0} VS {1} in {2}'.format(self.home_club_id.name, self.away_club_id.name, self.start_time)
    
class MatchDetail(models.Model):
    _name = 'generation.match_detail'
    _description = 'Match Detail'
    _inherit = ['generation.time']

    match_id = fields.Many2one('generation.match', 'Match')
    action = fields.Selection([ ('in', "In"),
                                ('out', "Out"),
                                ('score',"Score"),
                                ('throw', "Throw"),
                                ('free_kick_corner', "Free kick corner penalty"),
                                ('free_kick_penalty', "Free kick penalty"),
                                ('yellow_card', "Yellow Card"),
                                ('red_card', "Red Card"),
                                ])
    player_id = fields.Many2one('generation.player', 'Player')
    time = fields.Datetime('Time')


class Tag(models.Model):
    _name = 'generation.tag'
    _description = 'Tag'
    

class Post(models.Model):
    _name = 'generation.post'
    _description = 'Post'
    seo_name = fields.Char('SEO Name')
    seo_desc = fields.Text('SEO Desc')
    desc = fields.Text('Desc')
    content = fields.Text('Content')
    image = fields.Binary('Image')
    views = fields.Integer('Views')
    tag_ids = fields.Many2many('generation.tag', 'Tags')