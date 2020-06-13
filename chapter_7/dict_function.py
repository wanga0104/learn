heros = {'及时雨':'宋江','玉麒麟':'卢俊义','花和尚':'鲁智深','一丈青':'扈三娘'}
heros['豹子头']='林冲'
print(heros)
heros['及时雨'] = 'songjiang'
print(heros)
heros_star = {'母夜叉':'孙二娘'}
heros.update(heros_star)
print(heros)