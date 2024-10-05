# CSE PAGE Backend Part

## 최소 1회 실행 - 커밋시 자동으로 pre-commit 실행

```bash
pre-commit install
```

## 커밋 전 해당 명령어 수행 후 커밋

```bash
poetry run pre-commit run --all-files
```

## Alembic 설정

### 새로운 마이그레이션 생성

#### 1. 데이터베이스 구조 변경

#### 마이그레이션 진행

```bash
alembic revision --autogenerate -m "add migration message"
```

#### 마이그레이션 적용

```bash
alembic upgrade head
```

### 부록 1. 데이터베이스 백업

```bash
mysqldump -u username -p databasename > backup.sql
```

### 부록 2. 데이터베이스 복원

```bash
mysql -u username -p databasename < backup.sql
```

### 부록 3. alembic 다운그레이드

```bash
alembic current # 현재 버전 확인
alembic history # 과거 버전 기록 확인
```

```bash
alembic downgrade <revision ID>
```
