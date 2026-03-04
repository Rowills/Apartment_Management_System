# Apartment Community Management System (Django)

A Django + Django REST Framework backend for managing daily operations inside apartment or gated communities.

## Features
- Resident self-registration with approval workflow
- Role-based access control (Resident, Security, Association Staff, Admin)
- Maintenance ticketing lifecycle tracking
- Visitor entry and exit logs
- Notice board announcements
- Monthly fee invoices and payment tracking
- JWT authentication endpoints
- Dockerized local setup with PostgreSQL

## Domain Models
- **User**: custom auth model with role and approval status
- **Flat**: flat metadata and owner/resident mapping
- **Ticket**: maintenance issue tracking with category and status
- **VisitorLog**: security audit trail of visitors
- **Notice**: association broadcasts
- **FeeInvoice** and **Payment**: billing, payment records, and receipts

## API Endpoints
- `POST /api/token/` and `POST /api/token/refresh/`
- `/api/users/`
- `/api/flats/`
- `/api/tickets/`
- `/api/visitors/`
- `/api/notices/`
- `/api/fee-invoices/`
- `/api/payments/`

## Quick Start
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Or run with Docker:
```bash
docker compose up --build
```

## Notes
- Default database is PostgreSQL; configure via environment variables.
- `ownership_document` uploads are wired for local media and can be switched to S3-backed storage.
- Payment gateway integration stub is represented through `gateway_transaction_id` for extensibility.
