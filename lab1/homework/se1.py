import datetime
now = datetime.datetime.now()
from gmail import GMail,Message
html_content = '''
<p>Ch&agrave;o sếp,</p>
<p>S&aacute;ng nay ngủ dậy đột nhi&ecirc;n thấy ch&aacute;n qu&aacute; ,<strong> kh&ocirc;ng muốn đi l&agrave;m nữa</strong> , xếp cho e xin nghỉ 10 ng&agrave;y c&oacute; lương nh&eacute; iu sếp .&nbsp;&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-kiss.gif" alt="kiss" /></p>
<p>E Hiếu !</p>
'''
gmail = GMail("truonghieu05119x@gmail.com","Truongminhhieu0511")
msg = Message("đơn xin nghỉ hẳn", to="truonghieu0511@gmail.com",html=html_content)
if now.hour > 7:
    gmail.send(msg)
else:
    print("bh ko phai 7am") 
