###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################
stage.set_background("summer")


q1=codesters.Square(100, 100, 200,'Purple')
q2=codesters.Square(-100, 100, 200,'Violet')
q3=codesters.Square(-100, -100, 200,'BlueViolet')
q4=codesters.Square(100,- 100, 200,'Plum')


s1=codesters.Sprite("cool_dog", 100, 100)
s1.set_size(0.2)
s2=codesters.Sprite("Skz",-100, -100)
s2.set_size(0.6)
s3=codesters.Sprite("soccer", 100, -100)
s3.set_size(0.6)
s4=codesters.Sprite ("jungkook", -100, 100)
s4.set_size(0.6)