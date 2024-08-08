# CSE PAGE Backend Part

## install conda env in linux

```powershell
conda env create -f linux_environment.yaml
```

## install conda env in mac

```powershell
conda env create -f mac_environment.yaml
```

## install Postgresql in windows

### PostgreSQL installer

[PostgreSQL install](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)

### Microsoft VC++ runtime error 발생시

```powershell
postgresql-installer-windows.exe --install_runtimes 0
```

## init file name list

- csepage/database.py
- csepage/alembic.ini
