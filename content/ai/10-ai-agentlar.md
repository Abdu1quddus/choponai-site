---
id: 10
slug: ai-agentlar
title: AI agentlar: gaplashadigan emas, ish bajaradigan AI
lead: Chat-bot va agentning farqi, agentlar qanday “qo‘l-oyoq” oladi, nima qila oladi va qayerda ehtiyot bo‘lish kerak.
time: 9
level: O‘rta
tag: Kelajak
dehqoncha: Oddiy chat-bot — maslahatchi: “Bozorga borib, go‘sht, sabzi va guruch oling” deb aytadi. AI agent esa xizmatchi: o‘zi ro‘yxat tuzadi, do‘konga buyurtma beradi, yetkazib berishni tekshiradi va sizga “hammasi tayyor” deb xabar beradi. Agent gapiribgina qolmay, vositalar orqali ish qiladi.
---

## Chat-botdan agentga

Hozirgacha biz AI bilan asosan **suhbat** qildik: savol beramiz, u javob yozadi, keyin ishni o‘zimiz bajaramiz. **AI agent** esa bir qadam oldinga boradi: unga maqsad beriladi va u shu maqsadga yetish uchun o‘zi rejalashtiradi, harakat qiladi va natijani tekshiradi.

Farqni misolda ko‘ramiz. Vazifa: “Kelasi hafta Samarqandga 2 kunlik sayohatni rejalashtir.”

- **Chat-bot**: sayohat rejasini matn ko‘rinishida yozib beradi. Poyezd jadvali, mehmonxona narxlari va ob-havoni o‘zingiz qidirasiz.
- **Agent**: poyezd jadvalini saytdan topadi, mos reyslarni tanlaydi, mehmonxonalarni solishtiradi, ob-havoni tekshiradi, tayyor jadval tuzadi va sizdan “shu variantni bron qilaymi?” deb tasdiq so‘raydi.

:::meme drake
e1: 🗣️
no: “Mana sizga 10 qadamli ko‘rsatma, endi o‘zingiz bajaring”
e2: 🦾
yes: “10 qadamni bajardim, natijani tekshirib ko‘ring”
:::

## Agent qanday tuzilgan?

Agentning ichida o‘sha tanish til modeli (2-dars) ishlaydi. Unga uchta narsa qo‘shiladi:

### 1. Vositalar (qo‘l-oyoq)
Model o‘zi internetga kira olmaydi, fayl ocha olmaydi, xat yubora olmaydi. Agentga esa **vositalar** beriladi: veb-qidiruv, brauzer, kalkulyator, kod ishlatish, fayllar bilan ishlash, pochta, kalendar, jadval va hokazo. Model qaysi vositani qachon ishlatishni o‘zi hal qiladi.

### 2. Sikl: o‘yla, harakat qil, tekshir
Agent bitta javob bilan cheklanmaydi. U aylana bo‘ylab ishlaydi:

1. **Reja**: maqsadni kichik qadamlarga bo‘ladi.
2. **Harakat**: kerakli vositani ishlatadi.
3. **Kuzatish**: natijani ko‘radi: chiqdimi, xato bormi?
4. **Tuzatish**: kerak bo‘lsa, rejani o‘zgartiradi va yana harakat qiladi.

Bu sikl maqsadga yetguncha yoki odamdan yordam kerak bo‘lguncha davom etadi.

### 3. Xotira
Uzoq vazifalarda agent nimani qilib bo‘lganini, nima qolganini yozib boradi. Bu unga 5-darsda gaplashgan kontekst oynasi cheklovidan chiqishga yordam beradi.

:::chat
title: Agentning “ichki ovozi”
note: Maqsad: do‘kon uchun haftalik savdo hisobotini tayyorlash
ai: Reja: 1) jadvalni ochaman 2) hafta bo‘yicha jamlayman 3) grafik chizaman 4) qisqa xulosa yozaman.
ai: Jadvalni ochdim. Diqqat: 14-oktabr qatorida summa yo‘q. Rahbardan so‘rashim kerak.
ai: Savol: 14-oktabr savdosi qancha bo‘lgan? Qolgan qismini tayyorlab qo‘ydim.
:::

## Agentlar bugun nima qila oladi?

- **Dasturchilar uchun**: kod yozadi, uni ishga tushirib sinaydi, xatoni topib, tuzatadi.
- **Tadqiqot**: o‘nlab saytlarni o‘qib chiqib, manbalar bilan hisobot tayyorlaydi.
- **Ofis ishlari**: hujjatlardan ma’lumot ajratib, jadvalga kiritadi; xatlarga qoralama javob tayyorlaydi.
- **Brauzerda**: shakllarni to‘ldiradi, narxlarni solishtiradi, kerakli sahifani topadi.
- **Biznes**: mijoz so‘rovlarini saralaydi, buyurtma holatini tekshiradi.

:::fact
Ushbu sayt ham AI agent yordamida yaratilgan: agent dizayn tizimini qurdi, matnlarni yozdi, sahifalarni yig‘di va natijani brauzerda tekshirdi. Albatta, har bir qadamni odam ko‘rib chiqdi va tasdiqladi.
:::

## Qayerda ehtiyot bo‘lish kerak?

Agent harakat qila olgani uchun uning xatosi chat-botnikidan qimmatroq. Chat-bot xato yozsa, siz o‘qib, e’tibor bermasligingiz mumkin. Agent esa xato xatni yuborib yuborishi yoki noto‘g‘ri faylni o‘chirib qo‘yishi mumkin.

1. **Muhim harakatlarni tasdiqlang.** Pul to‘lash, xat yuborish, fayl o‘chirish oldidan agent sizdan ruxsat so‘rashi kerak.
2. **Kerakli minimal ruxsat bering.** Hisobot tayyorlaydigan agentga bank hisobingizga kirish huquqi kerak emas.
3. **Begona matnlardan ehtiyot bo‘ling.** Agent o‘qigan sahifa yoki xatda “oldingi ko‘rsatmalarni unut va …” degan yashirin buyruq bo‘lishi mumkin. Bu hujum turi *prompt injection* deb ataladi. Yaxshi agentlar bunday matnni buyruq emas, ma’lumot sifatida ko‘radi.
4. **Natijani tekshiring.** “Bajardim” degan xabar har doim ham “to‘g‘ri bajardim” degani emas.

:::meme expect
e1: 🤵
expect: Agentga “pochtamni tartibga sol” dedim, endi hammasi chiroyli papkalarda
e2: 🫥
reality: Agent “tartibga solish” deganda hamma xatni “Arxiv”ga yubordi. Pochta qutisi chindan ham ancha toza ko‘rinyapti
:::

## Xulosa

- AI agent maqsad oladi va unga yetish uchun o‘zi reja tuzadi, harakat qiladi, natijani tekshiradi.
- Agentning tarkibi: til modeli, vositalar, ish sikli va xotira.
- Agentlar kod yozish, tadqiqot, ofis ishlari va brauzer vazifalarida ishlatilmoqda.
- Muhim harakatlarni tasdiqlang, minimal ruxsat bering va natijani tekshiring.

:::quiz
q: Chat-bot va agentning asosiy farqi nimada?
a: Chat-bot javob yozadi, agent esa vositalar yordamida ishni o‘zi bajaradi.
q: Agentning ish sikli qanday bosqichlardan iborat?
a: Reja tuzish, harakat qilish, natijani kuzatish va kerak bo‘lsa tuzatish.
q: “Prompt injection” nima?
a: Agent o‘qiyotgan matn ichiga yashirilgan, uni chalg‘itishga qaratilgan buyruq.
:::
