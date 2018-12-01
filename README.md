## NJUPT_PE_class

没填写时TextBox1可视，填写时提交的是TextBox2

![pic1](https://github.com/Freedomisgood/NJUPT_PE_class/blob/master/readme/pic.jpg)

是这样的  比如我在一个输入框书写一个名字后  需要点击屏幕空白地区  来确认我输入的没问题

![pic1](https://github.com/Freedomisgood/NJUPT_PE_class/blob/master/readme/pic2.jpg)

```
ele_psw1 = driver.find_element_by_xpath('//*[@id="Textbox1"]')
ele_psw1.click()
nothing = driver.find_element_by_xpath('//*[@id="form1"]/div/div[2]/img')
nothing.click()
```

先点击输入框1，再转移焦点，再填写密码在输入框2中。

```
driver.switch_to.alert.accept()
```

点击弹窗的确认键
