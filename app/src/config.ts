import { defineConfig } from '@tok/generation';

export default defineConfig({
  // If you want to add language/currency localization – see ./examples/meditation as reference

  pages: [
    {
      slides: [
        // intro
        {
          media: {
            type: 'sticker',
            src: import('./assets/stickers/fox/chpic.su_-_ItsLisVK_022.tgs'),
            size: 250,
          },
          shape: 'square',
          pagination: 'count',
          title: 'Добро пожаловать в систему MarketBox',
          description:
            "Воспользуйтесь этим телеграм-приложением для активного взаимодействия с нашей командой и получения оперативной информации о продвижении работ по Вашему проекту<br><br>Это <b>просто</b>, <b>быстро</b>, <b>легко</b> и можно разобраться <a href='?page=1'>без инструкции</a>!",
          button: 'Далее',
        },

        // Инструкции
        {
          media: {
            type: 'sticker',
            src: import('./assets/stickers/fox/chpic.su_-_ItsLisVK_044.tgs'),
            size: 150,
          },
          shape: 'square',
          pagination: 'count',
          title: 'Видеоинструкция',
          description:
            'Инструкция по работе с системой разбита на логические видеоподкасты продолжительностью в несколько минут. Рекомендуется последовательно просмотреть весь материал, а затем, при необходимости, возвращаться к конкретным записям, чтобы освежить информацию или уточнить детали.',
          list: [
            {
              media: {
                type: 'icon',
                src: import('./assets/icons/num/2/number_1.svg'),
                
                size: 40,
              },
              text: "<a color: green; font-size: 1.5em' href='https://disk.yandex.ru/i/2HFj3Ygwu3dBuA' target='_blank'>Быстрый старт</a>",
            },
            {
              media: {
                type: 'icon',
                src: import('./assets/icons/num/2/number_2.svg'),
                
                size: 30,
              },
              text: "<a href='https://disk.yandex.ru/i/8K_fTBPW4_a3NQ' target='_blank'>Обзор web-интерфейса</a>",
            },
            {
              media: {
                type: 'icon',
                src: import('./assets/icons/num/2/number_3.svg'),
                
                size: 30,
              },
              text: "<a href='https://disk.yandex.ru/i/eUEFSK27zsqWIg' target='_blank'>Создание нового проекта</a>",
            },
            {
              media: {
                type: 'icon',
                src: import('./assets/icons/num/2/number_4.svg'),
                size: 30,
              },
              text: "<a href='https://disk.yandex.ru/i/2MFtYDNks7iY3A' target='_blank'>Вехи (ключевые этапы проекта)</a>",
            },
            {
              media: {
                type: 'icon',
                src: import('./assets/icons/num/2/number_5.svg'),
                size: 30,
              },
              text: "<a href='https://disk.yandex.ru/i/nxfLusvdl6iLrw' target='_blank'>Создание задач</a>",
            },
            {
              media: {
                type: 'icon',
                src: import('./assets/icons/num/2/number_6.svg'),
                size: 30,
              },
              text: "<a href='https://disk.yandex.ru/i/7vuTE9R5ZqDGrg' target='_blank'>Список задач проекта</a>",
            },
            {
              media: {
                type: 'icon',
                src: import('./assets/icons/num/2/number_7.svg'),
                size: 30,
              },
              text: "<a href='https://disk.yandex.ru/i/_4J_sQZZT39KKw' target='_blank'>Диаграмма Ганта</a>",
            },
            {
              media: {
                type: 'icon',
                src: import('./assets/icons/num/2/number_8.svg'),
                size: 30,
              },
              text: "<a href='https://disk.yandex.ru/i/LGlfKJlXCoxIoQ' target='_blank'>Доска задач</a>",
            },
            {
              media: {
                type: 'icon',
                src: import('./assets/icons/num/2/number_9.svg'),
                size: 30,
              },
              text: "<a href='https://disk.yandex.ru/i/bl_8HUh8R3Wn6A' target='_blank'>Варианты работы с задачами</a>",
            },
            {
              media: {
                type: 'icon',
                src: import('./assets/icons/num/2/number_10.svg'),
                size: 30,
              },
              text: "<a href='https://disk.yandex.ru/i/6FECcAGlyoc38w' target='_blank'>Работа со страницы задач</a>",
            },
            {
              media: {
                type: 'icon',
                src: import('./assets/icons/num/2/number_11.svg'),
                size: 30,
              },
              text: "<a href='https://marketbox.team/' target='_blank'>Работа на доске (KANBAN) - скоро</a>",
            },
            {
              media: {
                type: 'icon',
                src: import('./assets/icons/num/2/number_12.svg'),
                size: 30,
              },
              text: "<a href='https://marketbox.team/' target='_blank'>Доска MarketBox задачи (SCRUM) - скоро</a>",
            },
            {
              media: {
                type: 'icon',
                src: import('./assets/icons/num/2/number_13.svg'),
                size: 30,
              },
              text: "<a href='https://marketbox.team/' target='_blank'>Эффективное распределение задач по методологии Agile - скоро</a>",
            },
            /* {
              media: {
                type: 'icon',
                src: import('./assets/icons/num/2/number_10.svg'),
                size: 30,
              },
              text: "<a href='https://marketbox.team/' target='_blank'>SCRUM. Бэклог</a>",
            },
            {
              media: {
                type: 'icon',
                src: import('./assets/icons/num/2/number_11.svg'),
                size: 30,
              },
              text: "<a href='https://marketbox.team/' target='_blank'>SCRUM. Спринты</a>",
            },
            {
              media: {
                type: 'icon',
                src: import('./assets/icons/num/2/number_12.svg'),
                size: 30,
              },
              text: "<a href='https://marketbox.team/' target='_blank'>SCRUM. Приоритет</a>",
            },
            {
              media: {
                type: 'icon',
                src: import('./assets/icons/num/2/number_13.svg'),
                size: 30,
              },
              text: "<a href='https://marketbox.team/' target='_blank'>SCRUM. Распределение между исполнителями</a>",
            },
            {
              media: {
                type: 'icon',
                src: import('./assets/icons/num/2/number_14.svg'),
                size: 30,
              },
              text: "<a href='https://marketbox.team/' target='_blank'>SCRUM. Покер</a>",
            },
            {
              media: {
                type: 'icon',
                src: import('./assets/icons/num/2/number_15.svg'),
                size: 30,
              },
              text: "<a href='https://marketbox.team/' target='_blank'>Портфель проектов (группы проектов)</a>",
            }, */
          ],
          button: 'Далее',
        },

/* 
        // image
        {
          media: {
            type: 'image',
            src: import('./assets/img/marketing_strategy.jpg'),
          },
          shape: 'rounded',
          pagination: 'count',
          title: 'Графическое оформление',
          description:
            "Позволяет сделать акцент на  <b>Услуге</b>, или другом контексте...",
          button: 'Далее',
        },

        // form
        {
          extends: 'form', // note, it's important to extend from 'form' here
          media: {
            type: 'sticker',
            src: import('./assets/stickers/fox/chpic.su_-_ItsLisVK_044.tgs'),
            size: 150,
          },
          shape: 'square',
          pagination: 'count',
          title: 'Формы',
          description: 'Клиент заполняет форму – бот получает данные и можно обработать их, передать в <b>трекер</b>, отправить уведомление и прочие полезные действия...',
          form: [
            {
              id: 'text_from_form',
              placeholder: 'Ввод текста',
              type: 'text',
            },
            {
              id: 'number_from_form',
              placeholder: 'Ввод числа',
              type: 'number',
            },
            {
              id: 'checkbox_from_form',
              placeholder: 'Чекбокс',
              type: 'checkbox',
            },
          ],
          button: 'Далее',
        },

        // video
        {
          media: {
            type: 'video',
            src: import('./assets/videos/tags.mp4'),
            poster: import('./assets/img/spongebob_poster.webp'),
            style: 'aspect-ratio: 400/287', // here we manually set video aspect-ratio (default is 16:9)
          },
          shape: 'rounded',
          pagination: 'count',
          title: 'Видео-контент',
          description:
            "Можно сделать обучающий контент - <b>видеобиблиотеку</b> или видеопрезентации услуг, либо чего-то другого<br><br>Что позволит заинтересовать клиента и ознакомить с предложениями без необходимости посещения сайта.",
          button: 'Далее',
        },

        // list
        {
          media: {
            type: 'sticker',
            src: import('./assets/stickers/fox/chpic.su_-_ItsLisVK_008.tgs'),
            size: 150,
          },
          shape: 'square',
          pagination: 'count',
          title: 'Списки',
          description:
            'Списки можно использовать для демонстрации услуг или характеристик продукта. Элементы поддерживают настраиваемые значки',
          list: [
            {
              media: {
                type: 'icon',
                src: import('./assets/icons/guide.svg'),
                size: 30,
              },
              text: 'Какая-то крутая функция',
            },
            {
              media: {
                type: 'icon',
                src: import('./assets/icons/track.svg'),
                size: 30,
              },
              text: 'Очень крутая функция',
            },
            {
              media: {
                type: 'icon',
                src: import('./assets/icons/time.svg'),
                size: 30,
              },
              text: 'Некоторые чрезвычайно крутые функции',
            },
          ],
          button: 'Далее',
        },

        // go to paywall slide
        {
          media: {
            type: 'sticker',
            src: import('./assets/stickers/fox/chpic.su_-_ItsLisVK_013.tgs'),
            size: 250,
          },
          shape: 'square',
          pagination: 'count',
          textAlign: 'center',
          title: 'Но, это еще не все!',
          description: "Можно организовать платный доступ или оформление подписки...",
          button: {
            content: 'Перейти к оформлению услуги',
            to: '/paywall',
          },
        }, */
      ],
    },

    // paywall
    {
      extends: 'paywall',
      path: '/paywall',
      media: {
        type: 'sticker',
        src: import('./assets/stickers/fox/chpic.su_-_ItsLisVK_016.tgs'),
        size: 150,
      },
      shape: 'square',
      title: 'Оформить подписку на услуги',
      list: [
        'Можно настроить карточки продуктов',
        '<b>👛 Wallet Pay</b> и <b>Telegram Payments</b> можно подключить без лишних заморочек',
        'Можно организовать как подписки, так и разовые платежи',
      ],
      products: [
        {
          id: '1_month_subscription',
          title: 'Подписка на месяц',
          description: '1000$/месяц',
          discount: '',
          price: 1000,
        },
        {
          id: '1_year_subscription',
          title: 'Подписка на 1 год',
          description: '3600$/месяц',
          discount: 'Скидка 30%',
          price: 3600,
        },
        {
          id: 'lifetime_access',
          title: 'Пожизненный доступ',
          description: '20000$',
          discount: 'Лучшее предложение',
          price: 20000,
        },
      ],
      mainButtonText: 'Купить за {price}',
      popup: {
        // popup for payment methods choice
        type: 'web',
      },
      links: [
        {
          text: 'Политика конфиденциальности',
          href: 'https://google.com',
        },
        {
          text: 'Условия использования',
          href: 'https://google.com',
        },
      ],
    },
  ],
});
