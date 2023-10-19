from typing import Optional, Iterator

from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession
from sqlalchemy.orm import sessionmaker

import config


def create_engine(db_url: Optional[str] = None, execution_options: Optional[dict[str, str]] = None) -> AsyncEngine:
    return create_async_engine(
        db_url or config.DB_URL,
        pool_pre_ping=True,
        execution_options=execution_options,
    )


async_engine = create_engine()
AsyncSessionLocal = sessionmaker(
    bind=async_engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
)


async def session_scope() -> Iterator[AsyncSession]:
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception as e:
            await session.rollback()
            raise e
