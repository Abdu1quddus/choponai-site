---
id: 04
slug: ai-gallyutsinatsiyasi
title: AI nega ishonch bilan yolg‘on gapiradi?
lead: “Gallyutsinatsiya” nima, u qayerdan chiqadi va AI ning to‘qib chiqargan gaplaridan qanday himoyalanish kerak.
time: 9
level: Boshlang‘ich
tag: Xavfsizlik
dehqoncha: AI imtihonda javobni bilmasa ham jim turolmaydigan o‘quvchiga o‘xshaydi. Bilmagan savoliga ham ishonch bilan, chiroyli qilib javob yozib beradi. Bu javob ba’zan to‘g‘ri, ba’zan esa butunlay to‘qima chiqadi. Shuning uchun muhim gaplarni har doim tekshirish kerak.
---

## Gallyutsinatsiya nima?

AI ba’zan mavjud bo‘lmagan faktlarni, kitoblarni, odamlarni, raqamlarni yoki iqtiboslarni o‘ylab topadi va ularni xuddi haqiqatdek, hech ikkilanmasdan aytadi. Bu hodisa **gallyutsinatsiya** deyiladi.

Eng xavflisi shundaki, to‘qilgan javob ko‘rinishidan to‘g‘ri javobdan farq qilmaydi. Grammatikasi to‘g‘ri, ohangi ishonchli, hatto “manba” ham keltirilgan bo‘lishi mumkin. Faqat o‘sha manba umuman mavjud bo‘lmaydi.

:::chat
title: Klassik gallyutsinatsiya
user: Alisher Navoiyning Telegram haqidagi g‘azalidan iqtibos keltir.
ai: Albatta! Navoiy “Xabarlar devoni”da shunday yozgan: “Ko‘ngil xatin yetkurgan ul ko‘k qushdin…” Bu g‘azal Telegramning ramzi bo‘lgan ko‘k qushga bag‘ishlangan.
note: Navoiy XV asrda yashagan. Telegram 2013-yilda paydo bo‘lgan. “Xabarlar devoni” degan asar yo‘q, ko‘k qush esa umuman Twitter’ning belgisi edi 🤦
:::

Yangi modellar bunday ochiq-oydin xatolarni kamroq qiladi va ko‘pincha “bunday asar yo‘q” deb javob beradi. Lekin nozikroq mavzularda, masalan, aniq sanalar, statistika, kam ma’lum shaxslar, qonun moddalari yoki ilmiy maqolalarda, gallyutsinatsiya haligacha uchrab turadi.

## Nega bunday bo‘ladi?

2-darsni eslang: model keyingi so‘zni bashorat qiladi. U “bu to‘g‘rimi?” deb so‘ramaydi, u “bu yerda qaysi so‘z kelishi ehtimoli yuqori?” deb so‘raydi. Bundan uchta sabab kelib chiqadi.

1. **Model jim turishni yoqtirmaydi.** U javob berishga o‘rgatilgan. Savol berilgan bo‘lsa, eng ishonarli ko‘rinadigan javobni hosil qiladi.
2. **Ishonarli bilan to‘g‘ri bir xil narsa emas.** “Navoiy … devonida yozgan” degan jumla Navoiy haqidagi minglab matnlarga juda o‘xshaydi. Model uchun bu “normal” gap.
3. **Bilimlar siqilgan va xira.** Model ko‘rgan matnlarni so‘zma-so‘z saqlamaydi. Kam uchragan faktlar uning “xotirasi”da xiralashib qoladi va u bo‘shliqlarni o‘xshash narsalar bilan to‘ldiradi.

:::meme classic
top: Bilmasam ham
emoji: 😎
bottom: Shunday ishonch bilan aytamanki, o‘zim ham ishonib qolaman
caption: AI imtihonda
:::

## Qayerda eng ko‘p uchraydi?

Quyidagi mavzularda AI javobini ikki karra tekshiring:

- **Raqamlar va statistika**: aholi soni, narxlar, foizlar, sanalar.
- **Manbalar**: kitob nomlari, maqolalar, havolalar, sud qarorlari.
- **Kam ma’lum shaxslar va joylar**: mahalliy tadbirkorlar, kichik tashkilotlar, tumanlar tarixi.
- **Yangi voqealar**: model o‘qitilgandan keyin bo‘lgan hodisalar haqida u bilmaydi, agar internetdan qidirish funksiyasi bo‘lmasa.
- **Qonunlar, tibbiyot va moliya**: bu yerda xato qimmatga tushadi.

:::warn
Bir advokat sudga AI yozib bergan hujjatni topshirgan. Hujjatda keltirilgan oltita sud ishi umuman mavjud emas edi. Advokat jarimaga tortildi. AI ishlatish xato emas, uni tekshirmaslik xato.
:::

## Qanday himoyalanish kerak?

### 1. Manba so‘rang va uni o‘zingiz oching
“Bu ma’lumotning manbasini ko‘rsat” deb so‘rang. Lekin havolaning o‘zi kamlik qiladi, uni ochib, rostdan ham shu gap yozilganini tekshiring. Internetdan qidira oladigan AI vositalari (qidiruv rejimi) bu borada ishonchliroq.

### 2. “Bilmasang, bilmayman de” deb yozing
Bu oddiy jumla gallyutsinatsiyani sezilarli kamaytiradi. Model uchun “bilmayman” javobi ham ruxsat etilgan variantga aylanadi.

:::prompt Halol javob uchun
Quyidagi savolga javob ber. Agar aniq bilmasang yoki ishonching komil bo‘lmasa, “Aniq bilmayman” deb yoz va nimani tekshirish kerakligini ayt. Hech narsani o‘ylab topma.
Savol: ...
:::

### 3. Ma’lumotni o‘zingiz bering
AI ga savolni “bo‘sh qo‘l” bilan bermang. Hujjat, maqola yoki jadvalni o‘zingiz yuklang va “faqat shu matnga tayanib javob ber” deng. Bu holatda AI to‘qishdan ko‘ra, berilgan matndan foydalanadi.

### 4. Boshqa joyda tasdiqlang
Muhim raqam yoki faktni bitta ishonchli manbada (rasmiy sayt, kitob, mutaxassis) tekshirib ko‘ring. Ikkita turli AI ga bir xil savol berib, javoblarini solishtirish ham foydali signal beradi: ular har xil gapirsa, ehtiyot bo‘ling.

### 5. Javob juda silliq bo‘lsa, shubhalaning
Haqiqiy hayotda ma’lumotlar ko‘pincha chalkash va noaniq bo‘ladi. Agar AI javobi juda aniq, juda chiroyli va juda qulay bo‘lsa, bu ham tekshirish uchun sabab.

:::meme drake
no: AI aytdi, demak to‘g‘ri
yes: AI aytdi, demak tekshirib ko‘rishga arziydigan g‘oya
:::

## Gallyutsinatsiyaning foydali tomoni ham bor

Ijodiy ishlarda AI ning “o‘ylab topish” qobiliyati aynan kerak narsa. Ertak, reklama shiori, mahsulot nomi, she’r yoki yangi g‘oyalar uchun to‘qish yomon emas, aksincha, yaxshi. Muammo faqat **fakt** kerak bo‘lgan joyda **ijod** qilinganda yuzaga keladi.

:::chat
title: Ijod uchun — marhamat
user: Do‘konim uchun 5 ta qiziq nom o‘ylab top. Quruq meva sotaman.
ai: 1) Mag‘iz Saroyi 2) Bodom Bobo 3) Turshak Tayyor 4) Pista Planet 5) Yong‘oq Yo‘li
note: Bu yerda to‘qish — xizmat. Faqat nom bandligini tekshirishni unutmang 😉
:::

## Xulosa

- Gallyutsinatsiya: AI ning mavjud bo‘lmagan narsani ishonch bilan aytishi.
- Sababi: model to‘g‘rilikni emas, ishonarlilikni bashorat qiladi.
- Raqamlar, manbalar, yangi voqealar, qonun va tibbiyotda ayniqsa ehtiyot bo‘ling.
- Himoya: manba so‘rash, “bilmasang, ayt” deyish, ma’lumotni o‘zingiz berish va tekshirish.
- Ijodiy ishlarda esa to‘qish foydali.

:::quiz
q: AI nega mavjud bo‘lmagan kitobni “eslab” qoladi?
a: Chunki u to‘g‘rilikni tekshirmaydi, faqat ishonarli eshitiladigan matnni hosil qiladi.
q: Gallyutsinatsiyani kamaytiradigan eng oddiy jumla qaysi?
a: “Agar aniq bilmasang, bilmayman de, hech narsani o‘ylab topma.”
q: Qaysi vazifalarda AI ning to‘qishi foydali?
a: Ijodiy vazifalarda: nom, shior, ertak, g‘oya o‘ylab topishda.
:::
