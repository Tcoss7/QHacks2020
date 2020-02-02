import socket
from findEthicsScore import corporate_critic
from findEthicsScore import find_company

ethicscore = corporate_critic(find_company('https://www.amazon.ca/Nike-Mens-Tech-Essential-Belt/dp/B004RL0LCU/ref=sxin_0_ac_d_rm?ac_md=0-0-bmlrZQ%3D%3D-ac_d_rm&cv_ct_cx=nike&keywords=nike&pd_rd_i=B004RL0LCU&pd_rd_r=c54f7b06-4b31-4add-83c4-f64f2c5ec706&pd_rd_w=fVbVG&pd_rd_wg=pliWu&pf_rd_p=395c052b-36dd-4294-bb8c-6973256a7681&pf_rd_r=ZAQMGJ1ZSW5HKN85MFSB&psc=1&qid=1580593613&sr=1-1-12d4272d-8adb-4121-8624-135149aa9081'))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 1234))
s.listen(5)

while True:
	clientsocket, address = s.accept()
	print(f"connection from {address} is good")
	clientsocket.send(bytes(ethicscore, "utf-8"))
