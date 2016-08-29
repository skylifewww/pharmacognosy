# -*- coding: utf-8 -*-  

from django.contrib.auth.models import User
# from iosDevCourse.users.models import User
from django.db import models
from embed_video.fields import EmbedVideoField
from django.core.urlresolvers import reverse
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor_uploader.fields import RichTextUploadingField
import mptt
from mptt.fields import TreeForeignKey
import random
from django.conf import settings
from easy_thumbnails.fields import ThumbnailerImageField
# from content.models import Slide


def make_upload_path(instance, filename, prefix=False):
    n1 = random.randint(0, 10000)
    n2 = random.randint(0, 10000)
    n3 = random.randint(0, 10000)
    c = filename.split(".")
    filename = str(n1) + "_" + str(n2) + "_" + str(n3) + "." + c[-1]
    return u"%s/%s" % (settings.IMAGE_UPLOAD_DIR, filename)


# Create your models here.
class Category(MPTTModel):
    name = models.CharField(max_length=250, verbose_name=u"Имя категории", blank=True, default="", unique=True)
    parent = TreeForeignKey('self', related_name="children", blank=True, null=True, db_index=True, verbose_name="Родительский класс")

    def get_slides(self):
        return Slide.objects.filter(category=self)

    class Meta:
        db_table = "category"
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"
        ordering = ('tree_id','level')

    def __str__(self):
        return self.name

    class MPTTMeta:
        # level_attr = 'mptt_level'
        order_insertion_by = ['name']    


mptt.register(Category, order_insertion_by=['name'])




class Author(MPTTModel):
    slug = models.CharField(max_length=250, blank=True, verbose_name=u"Урл")
    name = models.CharField(max_length=200, verbose_name=u"Автор статьи", blank=True, default="", unique=True)
    parent = TreeForeignKey('self', related_name="children", blank=True, null=True, db_index=True, verbose_name="Родительский класс")

    class Meta:
        db_table = "authors"
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
        ordering = ('tree_id', 'level')

    def __str__(self):
        return self.name

    def pic_slug(self):
        if self.slug:
            return u'<img src="%s" width="70"/>' % self.slug
        else:
            return '(none)'
    pic_slug.short_description = u'Фото эксперта'
    pic_slug.allow_tags = True       

    class MPTTMeta:
        # level_attr = 'mptt_level'
        order_insertion_by = ['name']    


mptt.register(Author, order_insertion_by=['name'])


class Tag(models.Model):
    tag_name = models.CharField(max_length=50, verbose_name=u"Имя тега")
    # tag_name = models.CharField(max_length=50, verbose_name=u"Имя тега")

    class Meta:
        db_table = "tags"
        verbose_name = "теги"
        verbose_name_plural = "тег"

    def __str__(self):
        return self.tag_name


class Works(models.Model):
    work_author = models.CharField(max_length=50, verbose_name=u"автор", blank=True, null=True, default="")
    work_category = TreeForeignKey(Category, related_name="works", verbose_name=u"Категории", default="", blank=True)
    # image = ThumbnailerImageField(upload_to=make_upload_path, blank=True, verbose_name="картинка")
    slug = models.CharField(max_length=250, blank=True, verbose_name="Урл")
    short_text = RichTextUploadingField(blank=True, verbose_name="Короткое описание")
    work_title = models.CharField(max_length=50, verbose_name=u"Название товара")
    work_price = models.CharField(max_length=50, verbose_name=u"цена работы", blank=True, null=True, default="")

    class Meta:
        db_table = "works"
        verbose_name = "Примеры"
        verbose_name_plural = "Примеры"

    def __str__(self):
        return self.work_title

    # def pic(self):
    #     if self.image:
    #         return u'<img src="%s" width="70"/>' % self.image.url
    #     else:
    #         return '(none)'
    # pic.short_description = u'Большая картинка'
    # pic.allow_tags = True 

    def pic_slug(self):
        if self.slug:
            return u'<img src="%s" width="70"/>' % self.slug
        else:
            return '(none)'
    pic_slug.short_description = u'Изделие'
    pic_slug.allow_tags = True                  


class Article(models.Model):
    article_title = models.CharField(max_length=250, verbose_name=u"Название статьи")
    article_date = models.DateTimeField(verbose_name=u"Дата публикации статьи")
    # article_number = models.IntegerField(default=0, verbose_name="Номер статьи", blank=True, null=True)
    # article_likes = models.IntegerField(default=0, verbose_name="Лайки")
    article_tag = models.ManyToManyField(Tag, related_name=u"tags", related_query_name="tags", verbose_name=u"Теги")
    article_works = models.ManyToManyField(Works, related_name=u"works", related_query_name="works", verbose_name=u"Примеры работ", blank=True, default="")
    article_category = TreeForeignKey(Category, related_name="articles", verbose_name=u"Категории", default="", blank=True)
    article_author = TreeForeignKey(Author, related_name="autor", max_length=200, verbose_name=u"Автор статьи", blank=True, default="")
    short_text = RichTextUploadingField(blank=True, verbose_name="Короткое описание RU")
    # image = ThumbnailerImageField(upload_to=make_upload_path, blank=True, verbose_name="Шапка статьи")
    slug = models.CharField(max_length=250, blank=True, verbose_name="Урл")
    full_text = RichTextUploadingField(blank=True, verbose_name="Полное описание RU")
    article_video = EmbedVideoField(verbose_name='Видео', blank=True, help_text='URL video', null=True)
    video_published = models.BooleanField( blank=True, default="")
    video_only = models.BooleanField( blank=True, default="")
    text_published = models.BooleanField( blank=True, default="")
    written_only = models.BooleanField( blank=True, default="")
    
    
   

    def __str__(self):
        return self.article_title

    class Meta:
        db_table = 'article'
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ['-article_date']

    # def pic(self):
    #     if self.image:
    #         return u'<img src="%s" width="70"/>' % self.image.url
    #     else:
    #         return '(none)'
    # pic.short_description = u'Большая картинка'
    # pic.allow_tags = True  

    def pic_slug(self):
        if self.slug:
            return u'<img src="%s" width="70"/>' % self.slug
        else:
            return '(none)'
    pic_slug.short_description = u'Картинка статьи'
    pic_slug.allow_tags = True     

    

class Slide(models.Model):
    category = TreeForeignKey(Category, related_name="slides_article", verbose_name=u"Категория", default="", blank=True, null=True)
    name = models.CharField(max_length=250, verbose_name="Название")
    # image = models.ImageField(upload_to=make_upload_path, blank=True,  verbose_name="Изображение")
    slug = models.CharField(max_length=250, blank=True, verbose_name="Урл")
    text = RichTextUploadingField(blank=True, verbose_name="Короткое описание RU")
    published = models.BooleanField(verbose_name="Опубликован", blank=True)
    published_main = models.BooleanField(verbose_name="Опубликован на главной", default="", blank=True)
    ordering = models.IntegerField(verbose_name="Порядок сортировки", default=0, blank=True, null=True)
    
        
    def __str__(self):
        return self.name

    # def pic(self):
    #     if self.image:
    #         return u'<img src="%s" width="70"/>' % self.image.url
    #     else:
    #         return '(none)'
    # pic.short_description = u'Большая картинка'
    # pic.allow_tags = True

    def pic_slug(self):
        if self.slug:
            return u'<img src="%s" width="70"/>' % self.slug
        else:
            return '(none)'
    pic_slug.short_description = u'Слайд'
    pic_slug.allow_tags = True   

    class Meta:
        verbose_name_plural = "Слайды"
        verbose_name = "Слайд"  
    





