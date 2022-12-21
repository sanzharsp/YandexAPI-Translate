

## Yandex translate api example

Димонстрация API яндекс переводчика с использованием python requests и type hinting, говоря чисто пишешь, тревожным не будешь. Языки соответсвенно с русского на казахский но вы можете заменить их в переменных sourceLanguageCode с кокого переводить, targetLanguageCode на какой переводить



### `Для начало`

На странице биллинга убедитесь, что платежный аккаунт находится в статусе ACTIVE или TRIAL_ACTIVE. Если платежного аккаунта нет, создайте его.
Получите IAM-токен, необходимый для аутентификации.
Получите идентификатор любого каталога, на который у вашего аккаунта есть роль ai.translate.user или выше.

### https://cloud.yandex.ru/docs/translate/api-ref/authentication

### `type hinting`: https://kaznews.vercel.app/post/14
### `поставь звезду и не пожалеешь`
### .env 
Он состоит из 5 переменных <br>
<h4>URLS = https://translate.api.cloud.yandex.net/translate/v2/translate </h4>
<h4> TOKEN = <- IAM Token> </h4>
<h4>FOLDERID = < -folder id> - идентификатор каталога: https://console.cloud.yandex.ru/folders/ </h4>
<h4> ACCESS_TOKEN = <- Oauth Token> </h4>
<h4> TOKEN_REFRESH_URL = https://iam.api.cloud.yandex.net/iam/v1/tokens </h4>
## python version == 3.9.7

