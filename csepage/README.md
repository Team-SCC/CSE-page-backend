# Psql, Alembic

## 데이터베이스 변경

```sql
\c dbname
```

## 전체 테이블 조회

```sql
SELECT * FROM pg_catalog.pg_tables where schemaname = 'public';
```

## Alembic을 통한 migrations

```bash
alembic revision -m "message"
```
