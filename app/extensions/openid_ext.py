from flask_openid import OpenID
oid = OpenID(fs_store_path='./tmp/store', safe_roots=[])