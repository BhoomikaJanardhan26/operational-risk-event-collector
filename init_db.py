from services.db import engine, Base
from services.models import RiskLog

Base.metadata.create_all(bind=engine)

print("✅ Database created!")