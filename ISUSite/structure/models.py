from django.db import models
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from .validators import validate_pdf_file, validate_video_file
# Create your models here.


class NavBar(models.Model):
    NAVName = models.CharField(max_length=50, verbose_name="Navbar Title")
    NAVHasFather = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, verbose_name="Has Father?")
    NAVHtml = RichTextUploadingField( blank=True, null=True, verbose_name="Content HTML")
    NAVSlug = models.SlugField(blank=True, null=True, verbose_name="slug")

    def __str__(self):
        return self.NAVName

    def save(self, *args, **kwargs):
        if not self.NAVSlug:
            self.NAVSlug = 'nav'+str(slugify(self.id))
        super(NavBar, self).save(*args, **kwargs)


class Question(models.Model):
    QQuestion = models.CharField(max_length=100, verbose_name="The question")
    QAnswer = models.TextField( blank=True, null=True, verbose_name="The answer")

    def __str__(self):
        return self.QQuestion


class News(models.Model):
    NTitle = models.CharField(max_length=100, blank=True, null=True, verbose_name="News Title")
    NDetail = models.TextField( blank=True, null=True, verbose_name="default detail")
    NHtml = RichTextUploadingField(blank=True, null=True, verbose_name="Editable detail")
    NShort = models.TextField(blank=True, null=True, verbose_name="news short")
    NPdf = models.FileField(upload_to='news/files/', null=True, blank=True, verbose_name="File Upload", validators=[validate_pdf_file])
    NImage = models.ImageField(upload_to='news/', blank=True, null=True, verbose_name="news Image")    # blank=True, null=True,
    NDate = models.DateTimeField(verbose_name="news Date")

    def __str__(self):
        return self.NTitle

    def details(self):
        return self.NDetail[:50]+'.....'


class MotionImage(models.Model):
    MITitle = models.CharField(max_length=100, default="", verbose_name="Title")
    MIDetail = models.TextField(blank=True, null=True, verbose_name="Detail")
    MIImage = models.ImageField(upload_to='motion/', blank=True, null=True, verbose_name="Image")
    MIVisible = models.BooleanField(verbose_name="it's visible?")
    MIRelation = models.ForeignKey(NavBar, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Dedicated to")

    def __str__(self):
        return self.MITitle


class Adds(models.Model):
    ATitle = models.CharField(max_length=100, blank=True, null=True, verbose_name="Adds Title")
    ADetail = models.TextField(blank=True, null=True, verbose_name="default Detail")
    AHtml = RichTextUploadingField(blank=True, null=True, verbose_name="Editable detail")
    APdf = models.FileField(upload_to='adds/files/', null=True, blank=True, verbose_name="File Upload", validators=[validate_pdf_file])
    AImage = models.ImageField(upload_to='adds/', blank=True, null=True, verbose_name="Adds Image")  # , blank=True, null=True,
    ADate = models.DateTimeField(verbose_name="Adds Date")

    def __str__(self):
        return self.ATitle

    def details(self):
        return self.ADetail[:50] + '.....'


class Success(models.Model):
    STitle = models.CharField(max_length=100, verbose_name="Title")
    SDep = models.CharField(max_length=100, verbose_name="Department Name")
    SDetail = models.TextField(blank=True, null=True, verbose_name="default detail")
    SHtml = RichTextUploadingField(blank=True, null=True, verbose_name="Editable detail")
    SImage = models.ImageField(upload_to='success/', blank=True, null=True, verbose_name="primary Image")
    SVideo = models.FileField(upload_to='success/videos/', null=True, blank=True, verbose_name='Video upload', validators=[validate_video_file])

    def __str__(self):
        return self.STitle


class Contact(models.Model):
    CFacebook = models.CharField(max_length=150, blank=True, null=True, verbose_name="Facebook")
    CYoutube = models.CharField(max_length=150, blank=True, null=True, verbose_name="YouTube")
    CTelegram = models.CharField(max_length=150, blank=True, null=True, verbose_name="Telegram")
    CEmail = models.CharField(max_length=150, blank=True, null=True, verbose_name="Email")
    CAddress = models.CharField(max_length=150, blank=True, null=True, verbose_name="Address")
    CPhone = models.CharField(max_length=150, blank=True, null=True, verbose_name="Phone")


class Others(models.Model):
    OTitle = models.CharField(max_length=150, blank=True, null=True)
    ODetail = models.TextField(blank=True, null=True)


class Doctors(models.Model):
    DName = models.CharField(max_length=100, verbose_name="Name")
    DCareer = models.CharField(max_length=100, verbose_name="career")
    DAbout = RichTextUploadingField(blank=True, null=True, verbose_name="Editable about")
    DImage = models.ImageField(upload_to='doctors/', blank=True, null=True, verbose_name="primary Image")
    DFacebook = models.CharField(max_length=150, blank=True, null=True, verbose_name="Facebook")
    DLinkedin = models.CharField(max_length=150, blank=True, null=True, verbose_name="Linked in")
    DTwitter = models.CharField(max_length=150, blank=True, null=True, verbose_name="Twitter")

    def __str__(self):
        return self.DName


class Photo(models.Model):
    PName = models.CharField(max_length=100, verbose_name="Image Name")
    PImage = models.ImageField(upload_to='gallery/', verbose_name="Upload Image")

    def __str__(self):
        return self.PName
