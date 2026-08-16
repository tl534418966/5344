[app]
version = 1.0
title = 图片拼图工具
package.name = imgmerge
package.domain = org.imgmerge
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
requirements = python3,kivy
orientation = portrait
fullscreen = 0
#强制锁定编译工具版本
android.build_tools_version = 34.0.0
android.api = 33

[buildozer]
log_level = 2
warn_on_root = 1
