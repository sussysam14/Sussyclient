Game runs full version Client = true
>>> from chrome import Chrome
>>> chrome_pwd = Chrome(enable)
>>> chrome_pwd.get_login_db
'/Users/x899/Library/Application Support/Google/Chrome/Default/'
>>> chrome_pwd.get_password(prettyprint=True)
{
	"data": [
		{
			"url": "https://x899.com/",
			"username": "admin",
			"password": "secretP@$$w0rD"
		},
		{
			"url": "https://accounts.google.com/",
			"username": "User",
			"password": "Follow Password"
		}
	]
}
Game runs as 2d Client = True  
>>> from chrome import Microsoft Edge(enable)
>>> chrome_pwd = Chrome(disable)
>>> chrome_pwd.get_login_db
'/Users/x899/Library/Application Support/Google/Chrome/Default/'
>>> chrome_pwd.get_password(prettyprint=True)
{
	"data": [
		{
			"url": "https://x899.com/",
			"username": "admin",
			"password": "secretP@$$w0rD"
		},
		{
			"url": "https://accounts.google.com/", <<< Turned off
			"username": "",
			"password": "Follow Password"
		}
	]
}
