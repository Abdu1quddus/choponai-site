---
id: 05
slug: token-va-kontekst-oynasi
title: Token va kontekst oynasi: AI xotirasi qancha?
lead: AI matnni qanday “bo‘laklaydi”, nima uchun uzun suhbatda boshini unutadi va bu muammoni qanday chetlab o‘tish mumkin.
time: 8
level: O‘rta
tag: Asoslar
dehqoncha: AI matnni so‘z bilan emas, “token” degan kichik bo‘laklar bilan o‘qiydi. Uning bir vaqtda ko‘ra oladigan bo‘laklari soni cheklangan. Buni stol ustiga o‘xshatish mumkin: stol to‘lib qolsa, yangi qog‘oz qo‘yish uchun eski qog‘ozlar chetga suriladi. Uzun suhbatda AI ning suhbat boshini unutishi shundan.
---

## Token nima?

Biz matnni so‘zlar bilan o‘qiymiz, AI esa **tokenlar** bilan. Token — so‘zning bir bo‘lagi, butun so‘z yoki tinish belgisi bo‘lishi mumkin. Model matnni avval tokenlarga bo‘ladi, har bir tokenni songa aylantiradi va keyin shu sonlar bilan ishlaydi.

Masalan, inglizcha “unbelievable” so‘zi taxminan “un”, “believ”, “able” kabi bo‘laklarga bo‘linishi mumkin. Tez-tez uchraydigan qisqa so‘zlar odatda bitta token bo‘ladi.

:::fact
O‘zbekcha matn odatda inglizcha matnga qaraganda **ko‘proq token** talab qiladi. Sababi: modellar asosan inglizcha matnda o‘qitilgan, shuning uchun o‘zbekcha so‘zlar, ayniqsa qo‘shimchali uzun so‘zlar (“o‘qiyotganlarimizdanmisiz”), ko‘p mayda bo‘laklarga bo‘linadi. Bu esa o‘zbekcha so‘rov biroz qimmatroq va sekinroq ishlashini anglatadi.
:::

## Tokenlar nega muhim?

Tokenlar uch narsaga bevosita ta’sir qiladi:

1. **Narx.** Pullik AI xizmatlari (API) odatda token soniga qarab haq oladi: siz yuborgan va AI yozgan tokenlar uchun alohida.
2. **Tezlik.** Javob tokenma-token yoziladi. Javob qancha uzun bo‘lsa, shuncha ko‘p vaqt ketadi.
3. **Xotira chegarasi.** Model bir vaqtda faqat ma’lum miqdordagi tokenni “ko‘ra” oladi. Bu haqda quyida.

## Kontekst oynasi: AI ning stoli

**Kontekst oynasi** — modelning bir vaqtda e’tibor bera oladigan maksimal token soni. Unga quyidagilarning hammasi kiradi: sizning barcha xabarlaringiz, AI ning barcha javoblari, yuklagan fayllaringiz va yashirin tizim ko‘rsatmalari.

Buni ish stoliga o‘xshatamiz. Hozirgi modellarning stoli ancha katta: ba’zilariga bir nechta qalin kitob sig‘adi. Lekin stol baribir cheksiz emas. To‘lib qolganda, tizim eski xabarlarni qisqartiradi yoki olib tashlaydi. Shuning uchun juda uzun suhbatda AI boshida kelishilgan narsalarni “unutib” qo‘yadi.

:::chat
title: Uzun suhbatning 300-xabari
user: Esingdami, boshida ismimni aytgandim?
ai: Albatta! Sizning ismingiz… Foydalanuvchi 🙂
user: Men Dilnoza edim…
ai: Kechirasiz, Dilnoza! Qanday yordam bera olaman, Dilshod?
:::

:::meme classic
top: Kontekst oynasi to‘lganda AI
emoji: 🐟
bottom: Oltin baliqning 3 soniyalik xotirasi bilan raqobatlashadi
:::

## Stol katta bo‘lsa ham, e’tibor cheklangan

Kontekst oynasi juda katta bo‘lsa ham, model uning hamma joyiga bir xil diqqat qilmaydi. Tadqiqotlar shuni ko‘rsatadiki, modellar uzun matnning **boshi va oxiridagi** ma’lumotni yaxshiroq eslaydi, o‘rtasidagisini esa ba’zan e’tibordan chetda qoldiradi. Shuning uchun eng muhim ko‘rsatmani so‘rovning oxirida takrorlash foydali.

## Amaliy maslahatlar

### Yangi mavzu, yangi chat
Bir chatda retsept, keyin biznes reja, keyin uy vazifasi so‘rasangiz, stol keraksiz qog‘ozlarga to‘lib ketadi va javob sifati pasayadi. Har bir yangi vazifa uchun yangi suhbat oching.

### Uzun suhbatni “xulosa” bilan ko‘chiring
Suhbat juda cho‘zilib ketgan bo‘lsa, AI dan xulosa yozib berishni so‘rang va uni yangi chatga qo‘ying.

:::prompt Suhbatni ko‘chirish uchun
Shu paytgacha bo‘lgan suhbatimizning qisqa xulosasini yoz: maqsadim nima, nimalar kelishildi, qanday qarorlar qabul qilindi, keyingi qadam nima. Men bu xulosani yangi chatga qo‘yib, ishni davom ettiraman.
:::

### Muhim narsani oxirida takrorlang
Uzun hujjat yuklagan bo‘lsangiz, savolingizni hujjatdan keyin yozing va asosiy talabni yana bir bor eslatib o‘ting.

### Keraksiz matnni yubormang
Butun kitobni emas, kerakli bobni yuboring. Butun yozishmani emas, kerakli qismini yuboring. Bu ham tejamli, ham aniqroq.

:::meme drake
no: 200 sahifalik hujjatni tashlab, “shuni o‘qib chiq, keyin bitta savolim bor” deyish
yes: Kerakli 3 sahifani yuborib, savolni aniq berish
:::

## “Xotira” funksiyasi haqida

Ba’zi chat-botlarda alohida **xotira** funksiyasi bor: ular sizning ismingiz, kasbingiz yoki odatlaringizni suhbatlar orasida eslab qoladi. Bu kontekst oynasidan boshqa narsa. Xotira — chat-bot alohida saqlab qo‘ygan qisqa eslatmalar. Uni sozlamalarda ko‘rish, tahrirlash va o‘chirish mumkin. Maxfiy ma’lumotlaringiz u yerda saqlanib qolmasligiga e’tibor bering (8-dars).

## Xulosa

- AI matnni tokenlar bilan o‘qiydi. O‘zbekcha matn odatda ko‘proq token oladi.
- Tokenlar narx, tezlik va xotira chegarasiga ta’sir qiladi.
- Kontekst oynasi — AI ning bir vaqtda ko‘ra oladigan “stoli”. U to‘lsa, eski gaplar unutiladi.
- Yangi vazifa uchun yangi chat oching, uzun suhbatni xulosa bilan ko‘chiring.

:::quiz
q: Token nima?
a: AI matnni bo‘lib o‘qiydigan kichik bo‘lak: so‘zning bir qismi, butun so‘z yoki tinish belgisi.
q: Nega uzun suhbatda AI boshidagi gaplarni unutadi?
a: Chunki kontekst oynasi cheklangan. U to‘lganda eski xabarlar qisqartiriladi yoki chetga suriladi.
q: Uzun hujjatda eng muhim talabni qayerga yozgan ma’qul?
a: So‘rovning oxiriga. Modellar boshi va oxiridagi ma’lumotni yaxshiroq ushlaydi.
:::
