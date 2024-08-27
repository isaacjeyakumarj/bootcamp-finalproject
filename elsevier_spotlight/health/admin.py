from django.contrib import admin
# Register your models here.
from .models import healthblog,health1
from .utils import export_as_csv  # Import the CSV export function

admin.site.register(healthblog)




@admin.register(health1)
class YourModel1Admin(admin.ModelAdmin):
    list_display = ('id','title','name','slug','updated_on','content', 'created_on','status','categories','tags', 'text', 'image','image1', 'image2', 'author') # Customize your list display
    actions = [export_as_csv]  # Register the export action

