import os
import urlparse

env = os.environ.get("LOGISTICS_ENV","development")

db_url={}
db_url["development"] = os.environ.get("LOCAL_DATABASE_URL", "postgres://Eric:@localhost/instacart_dev")
db_url["read_only"] = os.environ.get("READ_ONLY_DATABASE_URL","postgres://localhost:5432/instacart_dev")
db_url["production"] = os.environ.get("DATABASE_URL","postgres://Eric:@localhost:5432/instacart_dev")
