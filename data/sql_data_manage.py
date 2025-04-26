from sqlalchemy.orm import Session

from db.sqlite import TableInfo, TableAlias, PromptRule

def get_table_info(db: Session, table_name: str = None):
    try:
        all_table = db.query(TableInfo).all() if table_name is None else \
            db.query(TableInfo).filter(TableInfo.table_name == table_name).all()
        all_table = [table.to_dict() for table in all_table]
    except Exception as e:
        print(e)
    return all_table

def update_table_info(db: Session, table_name: str, table_define_sql: str, table_field_info: str):
    try:
        table_info = db.query(TableInfo).filter(TableInfo.table_name == table_name).first()
        if table_info:
            table_info.table_define_sql = table_define_sql
            table_info.table_field_info = table_field_info
        else:
            new_table_info = TableInfo(
                table_name=table_name,
                table_define_sql=table_define_sql,
                table_field_info=table_field_info
            )
            db.add(new_table_info)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()

def delete_table_info(db: Session, table_name: str):
    try:
        table_info = db.query(TableInfo).filter(TableInfo.table_name == table_name).first()
        if table_info:
            db.delete(table_info)
            db.commit()
    except Exception as e:
        print(e)
        db.rollback()

def get_table_alias(db: Session, table_name: str = None):
    try:
        all_alias = db.query(TableAlias).all() if table_name is None else \
            db.query(TableAlias).filter(TableAlias.table_name == table_name).all()
        all_alias = [alias.to_dict() for alias in all_alias]
    except Exception as e:
        print(e)
    return all_alias

def create_table_alias(db: Session,table_name: str, table_alias: str, level: str):
    try:
        new_table_alias = TableAlias(
            table_name=table_name,
            table_alias=table_alias,
            level=level
        )
        db.add(new_table_alias)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()

def update_table_alias(db: Session, id:int, table_name: str, table_alias: str, level: str):
    try:
        table_alias_info = db.query(TableAlias).filter(TableAlias.id == id).first()
        if table_alias_info:
            table_alias_info.table_name = table_name
            table_alias_info.table_alias = table_alias
            table_alias_info.level = level
        else:
            raise ValueError("Table alias not found")
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()

def delete_table_alias(db: Session, id: int):
    try:
        table_alias_info = db.query(TableAlias).filter(TableAlias.id == id).first()
        if table_alias_info:
            db.delete(table_alias_info)
            db.commit()
    except Exception as e:
        print(e)
        db.rollback()

def get_prompt_rule(db: Session, step_type: str = None):
    try:
        all_prompt_rule = db.query(PromptRule).all() if step_type is None else \
            db.query(PromptRule).filter(PromptRule.step_type == step_type).all()
        all_prompt_rule = [rule.to_dict() for rule in all_prompt_rule]
    except Exception as e:
        print(e)
    return all_prompt_rule

def create_prompt_rule(db: Session, step_type: str, level: str, content: str):
    try:
        new_prompt_rule = PromptRule(
            step_type=step_type,
            level=level,
            content=content
        )
        db.add(new_prompt_rule)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()

def update_prompt_rule(db: Session, id: int, step_type: str, level: str, content: str):
    try:
        prompt_rule = db.query(PromptRule).filter(PromptRule.id == id).first()
        if prompt_rule:
            prompt_rule.step_type = step_type
            prompt_rule.level = level
            prompt_rule.content = content
        else:
            raise ValueError("Prompt rule not found")
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()

def delete_prompt_rule(db: Session, id: int):
    try:
        prompt_rule = db.query(PromptRule).filter(PromptRule.id == id).first()
        if prompt_rule:
            db.delete(prompt_rule)
            db.commit()
    except Exception as e:
        print(e)
        db.rollback()