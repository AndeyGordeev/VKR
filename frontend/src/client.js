import React from 'react'
import {render} from 'react-dom'
import {Provider} from 'react-redux'
import App from './components/app'
import configureStore from './redux/configureStore'

// Нужно создать то самое централизованное хранилище...
const store = configureStore();

render(
    // ... и завернуть приложение в специальный компонент,
    // умеющий с ним работать
    <Provider store={store}>
        <App/>
    </Provider>,
    document.querySelector('#app')
);
