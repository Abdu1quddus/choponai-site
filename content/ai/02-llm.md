---
id: 02
slug: chatgpt-qanday-oylaydi
title: ChatGPT qanday “o‘ylaydi”?
lead: Keyingi so‘zni topish o‘yini, milliardlab parametrlar va nima uchun AI har safar boshqacha javob beradi.
time: 9
level: Boshlang‘ich
tag: Asoslar
dehqoncha: Telefoningizda yozayotganda klaviatura keyingi so‘zni taklif qiladi-ku? ChatGPT ham xuddi shunday ishlaydi, faqat milliard marta kuchliroq. U gapning davomini eng mos keladigan so‘zlar bilan birma-bir to‘ldirib boradi. U “o‘ylamaydi”, lekin shunchalik yaxshi to‘ldiradiki, o‘ylayotgandek ko‘rinadi.
---

## LLM nima?

ChatGPT, Gemini, Claude va shunga o‘xshash chat-botlarning hammasi **katta til modeli** (inglizcha *Large Language Model*, qisqasi **LLM**) asosida ishlaydi. Nomining har bir so‘zi ma’noga ega:

- **Katta**, chunki ichida yuz milliardlab sozlanadigan son (parametr) bor.
- **Til**, chunki u matn bilan ishlaydi: o‘qiydi va yozadi.
- **Model**, chunki u tilning matematik “nusxasi”, ya’ni so‘zlar odatda qanday ketma-ketlikda kelishining juda murakkab xaritasi.

## Asosiy sir: keyingi so‘zni bashorat qilish

LLM ning butun ishi bitta savolga javob berishdan iborat: **“Shu matndan keyin qaysi so‘z kelishi ehtimoli eng yuqori?”**

Misol. Model quyidagi gapni ko‘rdi deylik:

> Osh — o‘zbek xalqining eng sevimli …

Model keyingi so‘z uchun ehtimollarni hisoblaydi. Taxminan shunday chiqadi:

- “taomi” — 81%
- “ovqati” — 12%
- “an’anasi” — 4%
- “sporti” — 0,001%

U “taomi” so‘zini tanlaydi, gapga qo‘shadi va **yangi gap uchun yana o‘sha savolni beradi**. So‘zma-so‘z, gapma-gap, butun javob shu tarzda quriladi. Siz ChatGPT javobi ekranda asta-sekin “yozilib” chiqayotganini ko‘rasiz. Bu shunchaki chiroyli effekt emas, model haqiqatan ham matnni bo‘lakma-bo‘lak hosil qilmoqda.

:::meme classic
top: Men o‘ylamayman
emoji: 🤖
bottom: Shunchaki keyingi so‘zni juda-juda yaxshi topaman
:::

## U buni qayerdan o‘rgangan?

Model o‘qitish jarayonida internetdagi ulkan hajmdagi matnni “o‘qib chiqqan”: kitoblar, maqolalar, forumlar, Vikipediya, dastur kodlari. Har bir gapda u keyingi so‘zni topishga harakat qilgan. Topolmasa, ichidagi parametrlar biroz to‘g‘rilangan. Trillionlab so‘z ustida shunday mashq qilingandan keyin model nafaqat grammatikani, balki faktlar, mantiq, uslub va hatto hazil qanday bo‘lishini ham “so‘zlarning odatiy ketma-ketligi” sifatida o‘zlashtirib olgan.

:::fact
Model o‘qigan matnlarning juda katta qismi ingliz tilida. O‘zbekcha matn internetda nisbatan kam, shuning uchun AI o‘zbek tilida ba’zan g‘alati iboralar ishlatadi yoki ruscha va turkcha so‘zlarni aralashtirib yuboradi. Yangi modellar bu borada tobora yaxshilanmoqda.
:::

## Nega u “aqlli” ko‘rinadi?

Agar model faqat keyingi so‘zni topsa, qanday qilib masala yechadi, she’r yozadi, kod tuzadi? Javobi shunda: keyingi so‘zni **juda yaxshi** topish uchun model dunyo haqida ko‘p narsani “bilishi” kerak bo‘ladi.

“Toshkent — O‘zbekistonning …” gapini to‘g‘ri davom ettirish uchun geografiyani bilish kerak. Matematika masalasining javobini topish uchun hisob-kitob qonuniyatlarini o‘zlashtirgan bo‘lishi kerak. Model shunchalik ko‘p matn ko‘rganki, bu bilimlar uning parametrlarida “siqilgan” holda saqlanadi.

Ammo bu bilim inson bilimidan farq qiladi. Model nima to‘g‘ri, nima noto‘g‘ri ekanini tekshirmaydi. U faqat nima **ishonarli eshitilishini** biladi. AI ning ishonch bilan xato gapirishi ham shundan kelib chiqadi (4-dars).

## Nega har safar boshqacha javob beradi?

Bir xil savolni ikki marta bersangiz, ikki xil javob olasiz. Sababi: model har doim eng ehtimolli so‘zni tanlamaydi. Unda **temperatura** degan sozlama bor.

- **Past temperatura**: model deyarli har doim eng ehtimolli so‘zni tanlaydi. Javoblar aniq, lekin zerikarli va bir xil bo‘ladi.
- **Yuqori temperatura**: model kamroq ehtimolli so‘zlarni ham tanlaydi. Javoblar ijodiyroq, lekin ba’zan bema’ni bo‘lib qoladi.

:::meme brain
l1: Osh — o‘zbek xalqining eng sevimli taomi.
l2: Osh — ota-bobolardan qolgan mazali an’ana.
l3: Osh — qozonda yozilgan dostonning birinchi bayti.
l4: Osh — koinotning sabzi va guruchdan iborat qora tuynugi.
caption: Temperaturani asta-sekin oshirib boramiz…
:::

## Chat-bot qanday qilib “odobli” bo‘lib qoldi?

Internetdagi matnni o‘qib chiqqan “xom” model shunchaki gapni davom ettiradi. U savolga javob berish o‘rniga, savolning davomini yozib ketishi ham mumkin. Uni yordamchiga aylantirish uchun yana bir bosqich bor: **odamlar fikri bilan o‘qitish**. Minglab odam model javoblarini baholaydi: bu foydali, bu qo‘pol, bu xavfli. Model yaxshi baholangan javoblarga o‘xshab yozishga o‘rgatiladi. Natijada u savolga javob beradigan, muloyim gapiradigan va zararli so‘rovlarni rad etadigan bo‘ladi.

## “O‘ylab javob beradigan” modellar

Yangi modellarning ko‘pida “fikrlash” rejimi bor. Bunday model javobdan oldin o‘zi uchun qoralama yozadi: masalani bo‘laklarga ajratadi, variantlarni solishtiradi, o‘zini tekshiradi. Bu ham o‘sha “keyingi so‘z” mexanizmi, lekin murakkab masalalarda natijani sezilarli yaxshilaydi. Shuning uchun matematik yoki mantiqiy masalalarda fikrlash rejimini yoqish foydali.

:::chat
title: “Tushundingmi?” savolining haqiqiy ma’nosi
user: Mening gapimni tushundingmi o‘zi?
ai: Ha, tushundim!
note: Aslida: “tushundim” so‘zi bu vaziyatda kelishi ehtimoli eng yuqori bo‘lgan so‘z edi.
:::

:::tip
AI ga uzun va murakkab vazifa berayotganda “Avval qadamma-qadam o‘ylab ko‘r, keyin javob ber” deb qo‘shib qo‘ying. Model o‘z mulohazasini yozib chiqqanda, xato qilish ehtimoli kamayadi.
:::

## Xulosa

- LLM — katta til modeli. ChatGPT, Gemini va Claude shu asosda ishlaydi.
- Uning asosiy ishi keyingi so‘zni bashorat qilish va javobni so‘zma-so‘z qurish.
- U internetdagi ulkan matnlardan o‘rgangan, shuning uchun ko‘p narsani “biladi”.
- Temperatura javobning qanchalik ijodiy bo‘lishini belgilaydi.
- Model haqiqatni tekshirmaydi, u faqat ishonarli matn yozadi.

:::quiz
q: LLM qisqartmasi nimani anglatadi?
a: Large Language Model, ya’ni katta til modeli.
q: Nega ChatGPT bir xil savolga har xil javob beradi?
a: Chunki u har doim eng ehtimolli so‘zni tanlamaydi. Temperatura sozlamasi tufayli javobga tasodifiylik qo‘shiladi.
q: Model gapirgan narsaning to‘g‘riligini o‘zi tekshiradimi?
a: Yo‘q. U faqat qaysi matn ishonarli eshitilishini biladi, shuning uchun muhim ma’lumotni o‘zingiz tekshirishingiz kerak.
:::
