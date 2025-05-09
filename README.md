
# 🛡️ Django Auth System – Register / Login / JWT / Protected Profile

## 📦 المتطلبات
- Python 3.8+
- Django 4.x
- Django REST Framework
- `djangorestframework-simplejwt`

---

## 🔧 خطوات الإعداد

### 1. إنشاء المشروع والتطبيق

```bash
django-admin startproject auth_project
cd auth_project
python manage.py startapp users
```

---

### 2. إضافة التطبيقات المطلوبة في `settings.py`

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'users',
]

TEMPLATES[0]['DIRS'] = [BASE_DIR / 'users' / 'Templates']
```

---

### 3. إعداد JWT في `settings.py`

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

from datetime import timedelta
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=1),
}
```

---

### 4. تثبيت الباكدجات المطلوبة

```bash
pip install djangorestframework djangorestframework-simplejwt bcrypt
```

---

### 5. إعداد الموديل `User` (اختياري لو استخدمت Custom User)
تم استخدام `AbstractBaseUser` أو `User` العادي في هذا المشروع.

---

### 6. إنشاء Serializer وAPI Views

- `serializers.py`: للتعامل مع البيانات
- `api_views.py`: لواجهة REST API (`RegisterAPIView`, `LoginAPIView`, `ProfileAPIView`)

---

### 7. ربط API URLs

```python
# users/api_urls.py

from django.urls import path
from .api_views import RegisterAPIView, LoginAPIView, ProfileAPIView

urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="register-api"),
    path("login/", LoginAPIView.as_view(), name="login-api"),
    path("profile/", ProfileAPIView.as_view(), name="profile-api"),
]
```

```python
# auth_project/urls.py

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("users.api_urls")),     # Endpoints API
    path("", include("users.urls")),             # صفحات HTML
]
```

---

### 8. إنشاء Views لعرض الصفحات

```python
# users/views.py

def login_page(request):
    return render(request, "login.html")

def register_page(request):
    return render(request, "register.html")

def profile_page(request):
    return render(request, "profile.html")
```

---

### 9. إعداد صفحات HTML داخل `users/Templates`

- `login.html`: واجهة تسجيل الدخول
- `register.html`: واجهة إنشاء حساب
- `profile.html`: واجهة محمية لعرض بيانات المستخدم

> كل صفحة مرتبطة بملف API عن طريق `fetch()` مع تصميم Bootstrap + Animations

---

### 10. استخدام JWT

- عند تسجيل الدخول: يتم إرسال البريد وكلمة السر إلى `/api/login/` ويُعاد JWT Token
- يتم حفظ التوكن في `localStorage`
- جميع الطلبات المحمية (مثل `/api/profile/`) يجب أن تحتوي على Header:  
  `Authorization: Bearer <token>`

---

## ✅ النتيجة النهائية

- تسجيل مستخدم جديد
- تسجيل دخول باستخدام API
- تخزين JWT واستعماله في الطلبات
- صفحة شخصية محمية
- تصميم Frontend جذاب باستخدام Bootstrap + Animations
