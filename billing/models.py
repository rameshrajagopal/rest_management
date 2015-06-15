from django.db import models
from django.template.defaultfilters import slugify

class FoodItem(models.Model):
    FOOD_CATEGORIES = (
            ('VEG DRY', 'VEG DRY'),
            ('NON VEG DRY', 'NON VEG DRY'),
            ('VEG TIFFIN', 'VEG TIFFIN'),
            ('NON VEG TIFFIN', 'NON VEG TIFFIN'),
            ('DESSERTS', 'DESSERTS'),
            ('COOL DRINKS', 'COOL DRINKS'),
            ('VEG', 'VEG'),
            ('NON-VEG', 'NON-VEG'),
            )
    name = models.CharField(max_length=128, unique=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='profile_images', blank=True)
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=32, choices=FOOD_CATEGORIES)
    times_ordered = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(FoodItem, self).save(*args, **kwargs)

class Bill(models.Model):
    TABLES = (
            ('1', 'TABLE 1'),
            ('2', 'TABLE 2'),
            ('3', 'TABLE 3'),
            ('4', 'TABLE 4'),
            ('5', 'TABLE 5'),
            ('6', 'TABLE 6'),
            )

    when = models.DateTimeField()
    total = models.FloatField()
    table = models.CharField(max_length=10, choices=TABLES, blank=True)

    def __str__(self):
        return 'BillNo {}'.format(self.id)

class BillInfo(models.Model):
    item = models.ForeignKey(FoodItem)
    quantity = models.FloatField()
    bill = models.ForeignKey(Bill)

class Goods(models.Model):
    GOODS_CATEGORIES = (
            ('vegtables', 'vegtables'),
            ('groceries', 'groceries'),
            ('gas', 'gas'),
            ('non-veg', 'non-veg'),
            ('others', 'others'),
            ('misc', 'misc'),
            ('dairy', 'dairy'),
            ('water', 'water'),
            )
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='profile_images', blank=True)
    category = models.CharField(max_length=32, choices=GOODS_CATEGORIES)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Goods, self).save(*args, **kwargs)

class GoodsBill(models.Model):
    when = models.DateTimeField()
    total = models.FloatField()
    merchant = models.CharField(max_length=128, blank=True)

class GoodsBillInfo(models.Model):
    item = models.ForeignKey(Goods)
    quantity = models.FloatField(default=0)
    bill = models.ForeignKey(GoodsBill)




