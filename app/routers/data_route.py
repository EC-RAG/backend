from typing import List
from fastapi import APIRouter, Depends, Query, Path, Response

from ..schemas.data_schema import *
from ..dependence import *

from data.sql_data_manage import *

data_router = APIRouter(prefix="/data", tags=["data"])

@data_router.get("/alltableinfo", response_model=List[TableData], tags=["tableinfo"])
async def handle_get_all_tables():
    return get_table_info()

@data_router.post("/addtableinfo", tags=["tableinfo"])
async def handle_add_table(data: TableData, db:Session = Depends(get_db)):
    try:
        update_table_info(db, **data.dict())
    except Exception as e:
        return Response(content=e.__str__, status_code=500)
    return True

@data_router.get("/rmtable", tags=["tableinfo"])
async def handle_remove_table(table_name: str = Query(..., description="Table name to remove"), db:Session = Depends(get_db)):
    try:
        delete_table_info(db, table_name)
    except Exception as e:
        return Response(content=e.__str__, status_code=500)
    return True

@data_router.post("/edittable", tags=["tableinfo"])
async def handle_update_table(data: TableData, db:Session = Depends(get_db)):
    try:
        update_table_info(db, **data.dict())
    except Exception as e:
        return Response(content=e.__str__, status_code=500)
    return True

@data_router.get("/gettable", tags=["tableinfo"])
async def handle_get_table(table_name: str = Query(..., description="Table name to get"), db:Session = Depends(get_db)):
    try:
        target_tables = get_table_info(db, table_name)
    except Exception as e:
        return Response(content=e.__str__, status_code=500)
    return target_tables

@data_router.get("/allalias", response_model=List[TableAlias], tags=["alias"])
async def handle_get_table_alias(db:Session = Depends(get_db)):
    try:
        table_alias = get_table_alias(db)
    except Exception as e:
        return Response(content=e.__str__, status_code=500)
    return table_alias

@data_router.get("/tabletags", response_model=list[str], tags=["alias"])
async def handle_get_table_tags(db:Session = Depends(get_db)):
    try:
        table_alias = get_table_alias(db)
        tags = set(map(lambda x: x["table_name"], table_alias))
    except Exception as e:
        return Response(content=e.__str__, status_code=500)
    return tags

@data_router.get("/rmalias", tags=["alias"])
async def handle_remove_alias(table_name: str = Query(..., description="Table name to remove alias"), db:Session = Depends(get_db)):
    try:
        delete_table_alias(db, table_name)
    except Exception as e:
        return Response(content=e.__str__, status_code=500)
    return True

@data_router.post("/editalias", tags=["alias"])
async def edit_alias(alias: TableAliasCreate, db:Session = Depends(get_db)):
    try:
        update_table_alias(db, **alias.dict(), level='user')
    except Exception as e:
        return Response(content=str(e), status_code=500)
    return True

@data_router.post("/addalias", tags=["alias"])
async def add_alias(alias: TableAliasCreate, db:Session = Depends(get_db)):
    try:
        update_table_alias(db, **alias.dict(), level='user')
    except Exception as e:
        return Response(content=str(e), status_code=500)
    return True

@data_router.get("/getalias", response_model=List[TableAlias], tags=["alias"])
async def handle_get_alias(table_name: str = Query(..., description="Table name to get alias"), db:Session = Depends(get_db)):
    try:
        target_alias = get_table_alias(db, table_name)
    except Exception as e:
        return Response(content=e.__str__, status_code=500)
    return target_alias

@data_router.get("/allrules", response_model=List[RuleData], tags=["rule"])
async def handle_get_all_rules(db:Session = Depends(get_db)):
    try:
        all_rules = get_prompt_rule(db)
    except Exception as e:
        return Response(content=e.__str__, status_code=500)
    return all_rules

data_router.get("/getrule", response_model=List[RuleData], tags=["rule"])
async def handle_get_rule(step_type: str = Query(..., description="Step type to get rule"), db:Session = Depends(get_db)):
    try:
        all_rules = get_prompt_rule(db, step_type)
    except Exception as e:
        return Response(content=e.__str__, status_code=500)
    return all_rules

data_router.post("/addrule", tags=["rule"])
async def handle_add_rule(rule: RuleCreate, db:Session = Depends(get_db)):
    try:
        create_prompt_rule(db, **rule.dict(), level='user')
    except Exception as e:
        return Response(content=e.__str__, status_code=500)
    return True

data_router.post("/editrule", tags=["rule"])
async def handle_edit_rule(rule: RuleUpdate, db:Session = Depends(get_db)):
    try:
        update_prompt_rule(db, **rule.dict(), level='user')
    except Exception as e:
        return Response(content=e.__str__, status_code=500)
    return True

data_router.get("/rmmrule", tags=["rule"])
async def handle_remove_rule(rule_id: int = Query(..., description="Rule ID to remove"), db:Session = Depends(get_db)):
    try:
        delete_prompt_rule(db, rule_id)
    except Exception as e:
        return Response(content=e.__str__, status_code=500)
    return True