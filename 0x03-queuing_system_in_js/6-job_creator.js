#!/usr/bin/node

import { createQueue } from 'kue';

const qe = createQueue();
const jobData = { phoneNumber: '+2347065345423', message: 'Kindly verify your identification' };

const job = qe
  .create('push_notification_code', jobData)
  .save((err) => {
    if (!err) console.log(`Notification job created: ${job.id}`);
  });

job.on('complete', (result) => { 
  console.log('Notification job completed');
});

job.on('failed', (err) => { 
  console.log('Notification job failed');
});