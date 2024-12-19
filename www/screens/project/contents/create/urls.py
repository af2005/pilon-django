from django.urls import path, include
from . import editor

urlpatterns = [

    path('default-editor', editor.view_default_editor,
         name="Content create with default editor"),
    path('markdown-editor', editor.view_markdown_editor,
         name="Content create with markdown editor"),
    path('file-upload', editor.view_file_upload, name="Content create with file upload")

]
