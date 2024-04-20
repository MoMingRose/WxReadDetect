# -*- coding: utf-8 -*-
# __init__.py.py created by MoMingLog on 19/4/2024.
"""
【作者】MoMingLog
【创建时间】2024-04-19
【功能描述】
"""
from fastapi import APIRouter

from app.api import callback_api_router

all_router = APIRouter(prefix="/mmlg")

all_router.include_router(callback_api_router, prefix="/callback")
