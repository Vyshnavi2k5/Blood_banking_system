const express = require('express');
const sequelize = require('./config/database');
const serviceRoutes = require('./Routes/serviceRoutes');
const teamRouting = require('./Routes/ourTeamRouting');
const contactRouting = require('./Routes/contactRouting');
const DonorRouting = require('./Routes/DonorRouting');  
const app = express();
const Path = require('path');
const cors = require('cors');
app.use(cors());

app.use(express.json());


require('./Models/service');
require('./Models/teams');
require('./Models/Contact');


sequelize.sync().then(() => {
    console.log("Database & tables synced!");
});
app.use('/image', express.static(Path.join(__dirname, 'public/image/')));

app.use('/api', serviceRoutes);
app.use('/api/team', teamRouting);
app.use('/api/contact', contactRouting);
app.use('/api/donor', DonorRouting);

app.listen(4000, () => {
    console.log("Server running on port 4000");
});