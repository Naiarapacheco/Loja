from django.db import models
from django.core.files import File

from io import BytesIO
from PIL import Image 

class Categoria(models.Model):
    nome = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome
    
class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='produtos', on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    slug = models.SlugField()
    descricao = models.TextField(blank=True, null=True) 
    preco = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True) 
    image = models.ImageField(upload_to='uploads/', blank=True, null=True) 
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.nome
    
    def get_preco_formatado(self):
        return f'R${self.preco:.2f}'
    
    #functionality to get the thumbnail
    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            return 'https://via.placeholder.com/240x240'     

     #if there are image but NO thumbnail        
    def make_thumbnail(self, image, size=(300, 300)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size) #generate automatically 

        #save to the server
        thumb_io = BytesIO() 
        img.save(thumb_io, 'JPEG', quality=85) #default quality '85'

        thumbnail = File(thumb_io, name=image.name) 

        return thumbnail 