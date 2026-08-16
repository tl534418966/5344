from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup
from kivy.graphics import Color, Rectangle
from PIL import Image
import os

class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.selected_paths = []

        self.btn_select = Button(text="选择多张图片", size_hint=(1,0.15))
        self.btn_select.bind(on_press=self.open_file_window)
        self.add_widget(self.btn_select)

        self.btn_export = Button(text="无损拼接导出", size_hint=(1,0.15))
        self.btn_export.bind(on_press=self.merge_img)
        self.add_widget(self.btn_export)

    def open_file_window(self, instance):
        content = BoxLayout(orientation="vertical")
        self.file_chooser = FileChooserListView(multiselect=True, filters=["*.png","*.jpg","*.jpeg"])
        btn_ok = Button(text="确定",size_hint=(1,0.12))
        content.add_widget(self.file_chooser)
        content.add_widget(btn_ok)
        self.pop = Popup(title="选取图片",content=content,size_hint=(0.95,0.9))
        btn_ok.bind(on_press=self.pick_img)
        self.pop.open()

    def pick_img(self,inst):
        self.selected_paths = self.file_chooser.selection
        self.pop.dismiss()

    def merge_img(self,inst):
        if not self.selected_paths:
            return
        im_list = []
        for p in self.selected_paths:
            img = Image.open(p)
            im_list.append(img.copy())
        #横向排布
        w_total = sum(i.width for i in im_list)
        h_max = max(i.height for i in im_list)
        new_img = Image.new("RGB",(w_total,h_max),color=(255,255,255))
        offset_x = 0
        for im in im_list:
            new_img.paste(im,(offset_x,0))
            offset_x += im.width
        save_dir = "/storage/emulated/0/DCIM"
        if not os.path.exists(save_dir):
            save_dir = "."
        out_path = os.path.join(save_dir,"merged_pic.jpg")
        new_img.save(out_path,quality=97)
        new_img.close()
        for i in im_list:
            i.close()

class MergeApp(App):
    def build(self):
        return MainLayout()

if __name__ == "__main__":
    MergeApp().run()
