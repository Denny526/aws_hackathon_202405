         ___        ______     ____ _                 _  ___  
        / \ \      / / ___|   / ___| | ___  _   _  __| |/ _ \ 
       / _ \ \ /\ / /\___ \  | |   | |/ _ \| | | |/ _` | (_) |
      / ___ \ V  V /  ___) | | |___| | (_) | |_| | (_| |\__, |
     /_/   \_\_/\_/  |____/   \____|_|\___/ \__,_|\__,_|  /_/ 
 ----------------------------------------------------------------- 
生成 SSH 密钥

step1. ssh-keygen -t rsa -b 4096 -C "your_email@example.com" #命令生成一个新的 SSH 密钥

step2. /home/ec2-user/.ssh/id_rsa #系统会提示你输入文件路径以保存密钥(預設)

step3. 建立password #提示你输入一个 passphrase

step4. 確認password #提示再次输入 passphrase 以确认

添加 SSH 密钥到 SSH 代理

step1. eval "$(ssh-agent -s)"

step2. ssh-add ~/.ssh/id_rsa

将 SSH 公钥添加到 GitHub

step1. cat ~/.ssh/id_rsa.pub #打开生成的公钥文件并复制内容

step2. 登录 GitHub，进入 “Settings” -> “SSH and GPG keys” -> “New SSH key”。 将公钥粘贴到 GitHub 上并保存。 密碼的開頭為ssh-rsa

配置 Git 远程仓库使用 SSH

step1. git remote set-url origin git@github.com:username/repository.git #将远程仓库的 URL 从 HTTPS 修改为 SSH

验证连接
step1. ssh -T git@github.com #命令测试 SSH 连接是否正常

step2. Hi username! You've successfully authenticated, but GitHub does not provide shell access. #如果配置正确，你应该会看到类似以下的信息：

 ----------------------------------------------------------------- 
上版語法與步驟

step1. cd sam    #移動到要上版的資料夾路徑 /

step2. git init  #初始化 Git  /

step3. git add . #添加所有文件 /

step4. git commit -m "Your commit message" #提交文件 /

step5. git remote add origin git@github.com:Denny526/Denny.git #配置 Git 远程仓库 /

step6. git push -u origin main  #推送文件到 GitHub (main 或 master) 

 ----------------------------------------------------------------- 