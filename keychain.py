from cadquery import *

txt = "CadQuery"
fontsize = 8

tag_l = 48
tag_w = 20
tag_h = 1.5
tag_hole_r = 2

tag = Workplane("XY").box(tag_l, tag_w, tag_h)
tag = tag.text(txt, fontsize, tag_h*2/3, font="Liberation Sans Bold")

tag = tag.union(
    cq.Workplane("XY")
    .cylinder(tag_h, tag_hole_r * 1.75)
    .translate((-tag_l/2, 0, 0))
).cut((
    cq.Workplane("XY")
    .cylinder(tag_h, tag_hole_r)
    .translate((-tag_l/2, 0, 0))
))

show_object(tag)