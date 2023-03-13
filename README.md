<p align="center">
  <b><font size="+6">Hospedamais SQLite</font></b>
</p>

Este é um projeto de um sistema de gestão hoteleira multi-empresas, com funcionalidades CRUD para cadastro de hóspedes, utilizando Django e SQLite.

![Tela de Hóspedes](https://github.com/NatalSantiago/ImagensProjetos/blob/master/TelaHospedes.png)

## Tecnologias utilizadas

- ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=flat-square)
- ![Django](https://img.shields.io/badge/-Django-092E20?logo=django&logoColor=white&style=flat-square)
- ![SQLite](https://img.shields.io/badge/-SQLite-003B57?logo=sqlite&logoColor=white&style=flat-square)
- ![JavaScript](https://img.shields.io/badge/-JavaScript-F7DF1E?logo=javascript&logoColor=black&style=flat-square)
- ![HTML5](https://img.shields.io/badge/-HTML5-E34F26?logo=html5&logoColor=white&style=flat-square)
- ![CSS3](https://img.shields.io/badge/-CSS3-1572B6?logo=css3&logoColor=white&style=flat-square)
- ![Visual Studio Code](https://img.shields.io/badge/-Visual%20Studio%20Code-007ACC?logo=visual-studio-code&logoColor=white&style=flat-square)

## Contato

- Whatsapp: [![WhatsApp](https://img.shields.io/badge/WhatsApp-Chat-green)](https://api.whatsapp.com/send?phone=5563992259154)
- E-mail: [![Gmail](https://img.shields.io/badge/Gmail-Email-red)](mailto:natal.santiago.filha@gmail.com)
- LinkedIn: [![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue)](https://www.linkedin.com/in/natal-santiago-986680257/)

### Como clonar e executar o projeto

# 1. Clone o repositório:

git clone https://github.com/NatalSantiago/hospedamais-sqlite.git

cd hospedamais-sqlite

# 2. Crie um ambiente virtual e ative-o:

python -m venv venv

source venv/bin/activate # Linux/Mac

venv\Scripts\activate # Windows

# 3. Instale as dependências do projeto:

pip install -r requirements.txt

# 4. Crie as tabelas do banco de dados:

python manage.py migrate

# 5. Crie um superusuário:

python manage.py createsuperuser
  
# 6. Execute o projeto:

python manage.py runserver
  
O projeto estará disponível em http://localhost:8000/.

# 7. Faça login no painel de administração usando as credenciais do superusuário criado anteriormente:

http://localhost:8000/admin/

# 8. Adicione novos hóspedes e gerencie os existentes usando as funcionalidades CRUD disponíveis.
