// Теперь, когда мы настроили сборку, 
// можно по-человечески импортировать.
import express from 'express'
import template from './src/template'

let app = express();

app.use('/dist', express.static('../dist'));

app.get("*", (req, res) => {
    res.send(template("VKR"));
});

app.listen(process.env.APP_FRONTEND_PORT);
