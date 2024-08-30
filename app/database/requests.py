from app.database.models import async_session
from app.database.models import User, Category, Item
from sqlalchemy import select, update, delete, desc

async def set_user(tg_id):
  async with async_session() as session:
    user = await session.scalar(select(User).where(User.id == tg_id))
    await session.commit()

async def get_categories():
  async with async_session() as session:
    return await session.scalars(select(Category))