import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
env_path = BASE_DIR / '.env'

if env_path.exists():
    with open(env_path, encoding='utf-8') as f:
        for line in f:
            if line.strip() and not line.startswith('#'):
                key, value = line.strip().split('=', 1)
                os.environ.setdefault(key, value)

SECRET_KEY = os.getenv('SECRET_KEY', 'fallback-secret-key')
assert SECRET_KEY, "SECRET_KEY is not set in environment"

DEBUG = True

ALLOWED_HOSTS = []


# Application 목록 추가
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',

    # allauth setting
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    
    # provider
    'allauth.socialaccount.providers.google',
]

# allauth setting 추가
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# allauth는 django.contrib.sites 프레임워크를 사용
SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware', # allauth 미들웨어 추가, 아마 장고 버전마다 필요한 버전이 따로 있는 것 같음 그냥 안정적으로 추가하는게 좋을 듯
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'config' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'config' / 'static',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 사용자가 로그인하거나 로그아웃했을 때, 어느 페이지로 이동시킬지 정해주는 설정
# 추가 다른 리다이렉트 설정이 있으면 묶어두어 관리하는 편
# 예를들어 Django account의 로그인같이 리다이렉트 설정이 많아지면 경로를 변수로 설정했던기억이있음 
LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'

# allauth 세부 설정 , 구글 소셜로 로그인 설정, 추가적으로 다른 소셜 로그인 설정도 여기에 추가 가능
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {        # 키와 비밀번호는 환경변수로 설정
            'client_id': os.getenv('GOOGLE_CLIENT_ID'),
            'secret': os.getenv('GOOGLE_SECRET_KEY'),
            'key': ''
        },
        'SCOPE': [      # 구글 소셜 로그인 시 요청할 권한
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {    # 구글 소셜 로그인 시 추가적인 파라미터
            'access_type': 'online',
        },
        'OAUTH_PKCE_ENABLED': True, # PKCE는 OAuth 2.0에서 보안성을 높이기 위해 사용되는 확장 기능
        #'METHOD': 'oauth2',  # 디폴트값으로 생략가능, 명시적으로 작성해도 무방
        #'VERIFIED_EMAIL': True,  # 이메일 인증된 사용자만 허용
        #'ID_TOKEN': True,  # ID 토큰 사용 설정
    }
}

#  회원가입 시 이메일 인증 비활성화 / 개발중엔 비활성화하여 빠르게 테스트
# 배포 이전에 잊지않고 활성화하고 테스트
ACCOUNT_EMAIL_VERIFICATION = 'none' 

# 다음작업 주석부분 추가 세팅 설정 완료 후 URL 설정으로 이동