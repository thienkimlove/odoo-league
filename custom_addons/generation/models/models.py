# -*- coding: utf-8 -*-
import logging
_logger = logging.getLogger(__name__)

from odoo import models, fields, api
from addons.http_routing.models.ir_http import slugify



class TimeModel(models.AbstractModel):
    _name = 'generation.time'


class Stadium(models.Model):
    _name = 'generation.stadium'
    _description = 'Sân vận động'
    name = fields.Char('Tên')
    active = fields.Boolean('Is Active?', default=True)
    slug = fields.Char("Slug", compute='_compute_slug')

    @api.depends('name')
    def _compute_slug(self):
        for r in self:
            r.slug = slugify(r.name)



class Season(models.Model):
    _name = 'generation.season'
    _description = 'Mùa'
    name = fields.Char('Tên')
    active = fields.Boolean('Is Active?', default=True)
    slug = fields.Char("Slug", compute='_compute_slug')

    @api.depends('name')
    def _compute_slug(self):
        for r in self:
            r.slug = slugify(r.name)


class Position(models.Model):
    _name = 'generation.position'
    _description = 'Vị trí thi đấu'
    name = fields.Char('Tên')
    active = fields.Boolean('Is Active?', default=True)
    slug = fields.Char("Slug", compute='_compute_slug')

    @api.depends('name')
    def _compute_slug(self):
        for r in self:
            r.slug = slugify(r.name)

class League(models.Model):
    _name = 'generation.league'
    _description = 'Giải đấu'
    name = fields.Char('Tên')
    active = fields.Boolean('Is Active?', default=True)
    slug = fields.Char("Slug", compute='_compute_slug')

    @api.depends('name')
    def _compute_slug(self):
        for r in self:
            r.slug = slugify(r.name)

    season_id = fields.Many2one('generation.season', 'Season')

class Club(models.Model):
    _name = 'generation.club'
    _description = 'Câu lạc bộ'
    name = fields.Char('Tên')
    active = fields.Boolean('Is Active?', default=True)
    slug = fields.Char("Slug", compute='_compute_slug')

    @api.depends('name')
    def _compute_slug(self):
        for r in self:
            r.slug = slugify(r.name)

    image = fields.Binary('Ảnh')
    stadium_id = fields.Many2one('generation.stadium', 'Stadium')

class Player(models.Model):
    _name = 'generation.player'
    _description = 'Cầu thủ'
    name = fields.Char('Tên')
    active = fields.Boolean('Is Active?', default=True)
    slug = fields.Char("Slug", compute='_compute_slug')

    @api.depends('name')
    def _compute_slug(self):
        for r in self:
            r.slug = slugify(r.name)

    dob = fields.Date('Ngày sinh')
    country_id = fields.Many2one('res.country', 'Quốc tịch')
    height = fields.Integer('Chiều cao')
    weight = fields.Integer('Cân nặng')
    position_id = fields.Many2one('generation.position', 'Vị trí')
    club_id = fields.Many2one('generation.club', 'Câu lạc bộ')
    club_join_date = fields.Date('Ngày gia nhập')
    image = fields.Binary('Ảnh')

    @api.model
    def create(self, vals):
        record = super(Player, self).create(vals)

        # Logging debug messages
        _logger.debug('Current record %s', repr(record))

        self.env['generation.history'].create({ 'club_id' : record.club_id.id, 'player_id' : record.id, 'club_join_date' : record.club_join_date })
        return record

    @api.multi
    def write(self, vals):
        super(Player, self).write(vals)

        # Logging debug messages
        _logger.debug('Current record %s', repr(vals))
        self.env['generation.history'].create({ 'club_id' : self.club_id.id, 'player_id' : self.id, 'club_join_date' : self.club_join_date })
        return True



class Referee(models.Model):
    _name = 'generation.referee'
    _description = 'Trọng tài'
    name = fields.Char('Tên')
    active = fields.Boolean('Is Active?', default=True)
    slug = fields.Char("Slug", compute='_compute_slug')

    @api.depends('name')
    def _compute_slug(self):
        for r in self:
            r.slug = slugify(r.name)

    dob = fields.Date('Ngày sinh')
    country_id = fields.Many2one('res.country', 'Quốc tịch')
    height = fields.Integer('Chiều cao')
    weight = fields.Integer('Cân nặng')
    image = fields.Binary('Ảnh')

class Coach(models.Model):
    _name = 'generation.coach'
    _description = 'Huấn luyện viên'
    name = fields.Char('Tên')
    active = fields.Boolean('Is Active?', default=True)
    slug = fields.Char("Slug", compute='_compute_slug')

    @api.depends('name')
    def _compute_slug(self):
        for r in self:
            r.slug = slugify(r.name)

    dob = fields.Date('Ngày sinh')
    country_id = fields.Many2one('res.country', 'Quốc tịch')
    height = fields.Integer('Chiều cao')
    weight = fields.Integer('Cân nặng')
    image = fields.Binary('Ảnh')
    club_id = fields.Many2one('generation.club', 'Câu lạc bộ')

class Match(models.Model):
    _name = 'generation.match'
    _description = 'Trận đấu'

    active = fields.Boolean('Is Active?', default=True)
    slug = fields.Char("Slug", compute='_compute_slug')



    name = fields.Char('Tên', readonly=1, compute='_compute_match_name')

    home_club_id = fields.Many2one('generation.club', 'Đội 1 (Nhà)',)
    away_club_id = fields.Many2one('generation.club', 'Đội 2 (Khách)')

    start_home_player_ids = fields.Many2many('generation.player', string='Đội hình xuất phát đội 1', domain="[('club_id','=',home_club_id)]")
    start_away_player_ids = fields.Many2many('generation.player', string='Đội hình xuất phát đội 2',  domain="[('club_id','=',away_club_id)]")
    referee_id = fields.Many2one('generation.referee', 'Trọng tài')
    start_time = fields.Datetime('Giờ bắt đầu')
    end_time = fields.Datetime('Giờ kết thúc')
    league_id = fields.Many2one('generation.league', 'Giải đấu')
    stadium_id = fields.Many2one('generation.stadium', 'Sân vận động')
    home_score = fields.Integer('Tỉ số chung cuộc đội 1')
    away_score = fields.Integer('Tỉ số chung cuộc đội 2')
    match_detail_ids = fields.One2many(
        'generation.match_detail',
        'match_id',
        'Chi tiết trận đấu')

    @api.depends('home_club_id.name', 'away_club_id.name', 'start_time')
    def _compute_match_name(self):
        for r in self:
            r.name = '{0} VS {1} vào lúc {2}'.format(self.home_club_id.name, self.away_club_id.name, self.start_time)

class MatchEvent(models.Model):
    _name = 'generation.match_event'
    _description = 'Sự kiện trong trận đấu'

    name = fields.Char('Tên')
    active = fields.Boolean('Is Active?', default=True)
    slug = fields.Char("Slug", compute='_compute_match_event_slug')

    @api.depends('name')
    def _compute_match_event_slug(self):
        for r in self:
            r.slug = slugify(r.name)

class MatchDetail(models.Model):
    _name = 'generation.match_detail'
    _description = 'Chi tiết trận đấu'

    active = fields.Boolean('Is Active?', default=True)
    slug = fields.Char("Slug", compute='_compute_slug')



    name = fields.Char('Tên', readonly=1, compute='_compute_match_detail_name')

    match_id = fields.Many2one('generation.match', 'Trận đấu')
    match_event_id = fields.Many2one('generation.match_event', 'Sự kiện')
    player_id = fields.Many2one('generation.player', 'Cầu thủ')
    time = fields.Datetime('Thời gian')

    @api.depends('player_id.name', 'match_event_id.name', 'time')
    def _compute_match_detail_name(self):
        for r in self:
            r.name = '{0} {1} vào lúc {2}'.format(self.player_id.name, self.match_event_id.name,self.time)


class Post(models.Model):
    _name = 'generation.post'
    _description = 'Bài viết'
    name = fields.Char('Tên')
    active = fields.Boolean('Is Active?', default=True)
    slug = fields.Char("Slug", compute='_compute_slug')

    @api.depends('name')
    def _compute_slug(self):
        for r in self:
            r.slug = slugify(r.name)

    seo_name = fields.Char('SEO Name')
    seo_desc = fields.Text('SEO Desc')
    desc = fields.Text('Mô tả')
    content = fields.Text('Nội dung')
    image = fields.Binary('Ảnh')
    views = fields.Integer('Lượt xem')
    tag_ids = fields.Many2many('generation.tag', string='Tags')


class History(models.Model):
    _name = 'generation.history'
    _description = 'Lịch sử thi đấu'
    _rec_name = 'player_id'
    player_id = fields.Many2one('generation.player', string='Cầu thủ')
    club_id = fields.Many2one('generation.club', string='Câu lạc bộ')
    club_join_date = fields.Date('Ngày gia nhập')

class Tag(models.Model):
    _name = 'generation.tag'
    _description = 'Từ khóa'
    name = fields.Char('Tên')
    active = fields.Boolean('Is Active?', default=True)
    slug = fields.Char("Slug", compute='_compute_tag_slug')
    @api.depends('name')
    def _compute_tag_slug(self):
        for r in self:
            r.slug = slugify(r.name)

