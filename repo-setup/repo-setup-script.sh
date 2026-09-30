# 1. Create root directory and shared folders
mkdir -p information-engineering-course/{assets,docs,lab-environment/scripts}

# 2. Generate unit folders (01 to 21) with standardized subdirectories and READMEs
for i in $(seq -w 1 21); do
  mkdir -p information-engineering-course/units/unit-$i/{slides,code,exercises}
  echo "# Unit $i" > information-engineering-course/units/unit-$i/README.md
done

cd information-engineering-course

# 3. Create root README.md
cat << 'EOF' > README.md
# Information Systems Engineering (Level 6) - 2026/27

Welcome to the central repository for Information Systems Engineering.

## Navigation & Structure
- `docs/`: Module specification, assignment briefs, and setup guides.
- `lab-environment/`: Shared Docker Compose stack for local hands-on labs.
- `units/`: Sequenced curriculum units (Units 01 to 21).
EOF

# 4. Create root docker-compose placeholder
cat << 'EOF' > lab-environment/docker-compose.yml
version: '3.8'
services:
  postgres:
    image: postgres:15
    environment:
      POSTGRES_PASSWORD: postgrespassword
    ports:
      - "5432:5432"
EOF

# 5. Initialize Git and commit
git init
git branch -M main
git add .
git commit -m "feat: initialize 21-unit course directory structure"