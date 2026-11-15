# 🌙 FORGE NEO — Dark Fantasy Theme

**Dark Fantasy** — отдельное расширение для [Forge NEO](https://github.com/Haoming02/sd-webui-forge-classic/tree/neo) с тёмным оформлением, золотыми рамками и фиолетовыми магическими акцентами.

✨ **Версия:** 1.2 · **Автор:** [NevskiyArt](https://github.com/NevskiyArt) · **Совместимость:** Forge NEO

> ⚠️ Это оформление **для Forge NEO**, а не отдельная сборка генератора и не тема для ComfyUI. Полноценное тестирование на различных установках Forge NEO пока не проводилось. Если установлены другие темы, их CSS может конфликтовать с этим расширением.

## ✨ Возможности

- 🌑 Тёмно-синие и обсидиановые панели.
- ✨ Золотые рамки и аккуратные контуры блоков.
- 💜 Фиолетовая подсветка активных вкладок, ползунков и кнопки **Generate**.
- 🔮 Заголовок **FORGE NEO**.
- ⚙️ Переключение между стандартным оформлением и Dark Fantasy в настройках Forge NEO.
- 🧩 Без внешних библиотек, сетевых запросов или изменения файлов основного интерфейса.

## 📥 Установка через Forge NEO

1. Откройте Forge NEO → **Extensions** → **Install from URL**.
2. Вставьте адрес репозитория:

   ```text
   https://github.com/NevskiyArt/forge-neo-dark-fantasy
   ```

3. Нажмите **Install**.
4. Перезапустите Forge NEO, затем обновите страницу сочетанием `Ctrl + F5`.
5. Откройте **Settings → FORGE NEO — тема**.
6. В пункте **Оформление FORGE NEO** выберите **Dark Fantasy** и нажмите **Apply settings**.

### Ручная установка

Скачайте репозиторий как ZIP и распакуйте папку `forge-neo-dark-fantasy` в каталог `extensions` вашей установки Forge NEO.

Проверьте структуру:

```text
Forge NEO/
└── extensions/
    └── forge-neo-dark-fantasy/
        ├── scripts/
        │   └── dark_fantasy.py
        └── javascript/
            └── dark_fantasy.js
```

После установки перезапустите Forge NEO и выберите тему в настройках.

> **Важно:** если раньше устанавливали CSS-версию темы через `user.css`, сделайте резервную копию файла и удалите из него только правила старой темы — иначе старое оформление может оставаться включённым при выборе «Стандартная».

## 🔁 Как вернуть стандартную тему

Перейдите в **Settings → FORGE NEO — тема**, выберите **Стандартная**, нажмите **Apply settings**. Перезапуск обычно не требуется. При необходимости обновите страницу браузера.

Чтобы полностью удалить тему, отключите её на вкладке **Extensions** или удалите папку `extensions/forge-neo-dark-fantasy` при выключенном Forge NEO.

## 🆕 Что нового в v1.2

- Исправлено перекрытие системных кнопок **Interrupt** и **Skip** кнопкой Generate.
- Добавлено отдельное контрастное оформление Interrupt и Skip.
- Во время генерации панель кнопок мягко пульсирует; анимация отключается при системной настройке уменьшения движения.

## 🛠️ Как устроено

- `scripts/dark_fantasy.py` — добавляет выбор оформления в настройки Forge NEO.
- `javascript/dark_fantasy.js` — применяет CSS только при выборе Dark Fantasy и убирает его при возврате к стандартной теме.
- `README_RU.txt` — краткая подробная инструкция на русском.

Расширение не изменяет модели, промпты, параметры генерации или код Forge NEO.

## ⚠️ Статус

**1.2 — тестовая версия.** Регистрация настроек и логика переключения проверены на уровне кода, но поведение может отличаться между версиями Gradio/Forge NEO и сторонними расширениями. Сообщайте о проблемах во вкладке **Issues**, желательно со скриншотом интерфейса и версией Forge NEO.

---

<details>
<summary>🇬🇧 English installation guide</summary>

### FORGE NEO — Dark Fantasy Theme

An optional visual theme extension for **Forge NEO**, featuring obsidian-blue panels, subtle gold framing and violet accents. Version 1.2 is an early test release.

1. Open Forge NEO → **Extensions** → **Install from URL**.
2. Paste `https://github.com/NevskiyArt/forge-neo-dark-fantasy` and install.
3. Restart Forge NEO, then use `Ctrl + F5` in your browser.
4. Open **Settings → FORGE NEO — тема**, select **Dark Fantasy** in the **Оформление FORGE NEO** option and click **Apply settings**.
5. Select **Стандартная** in the same setting to revert.

This is a Forge NEO extension, not a replacement UI. It changes appearance only, and may conflict with other CSS themes. If you previously used a standalone `user.css` version, remove only its Dark Fantasy rules to avoid overlap.

</details>
