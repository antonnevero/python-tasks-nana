from user import User
from post import Post

Anton = User("nn@gmal.com", "Anton", "12345", "DevOps")
Anton.change_job_title("DevOps engineer")
Anton.get_user_info()

Veronika = User("vv@gmail.com", "Nika", "11111", "Nail Master")
Veronika.get_user_info()

new_post = Post("on a secret mission today", Anton.name)
new_post.get_post_info()