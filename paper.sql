drop database paper;
create database paper default character set utf8 collate utf8_general_ci;
use paper;

create table users(
  user_id int(11) unsigned not null auto_increment,
  username varchar(32) not null,
  password varchar(32) not null,
  email varchar(255) not null,
  status tinyint(1) not null default 1,
  admin tinyint(1) not null default 0,
  vip tinyint(1) not null default 0,
  primary key (user_id)
) default charset=utf8;

create table companies(
  company_id int(11) unsigned not null auto_increment,
  company_name varchar(255) not null,
  introduction text,
  picture varchar(255) not null default '/static/img/company/company.png',
  primary key (company_id)
) default charset=utf8;

create table papers(
  paper_id int(11) unsigned not null auto_increment,
  company_id int(11) unsigned not null,
  paper_name varchar(255) not null,
  constraint papers_company_id foreign key (company_id) references companies (company_id) on delete cascade on update cascade,
  primary key (paper_id)
) default charset=utf8;

create table questions(
  question_id int(11) unsigned not null auto_increment,
  content text,
  answer text,
  ques_type smallint(2) not null default 1,
  paper_id int(11) unsigned not null,
  constraint questions_paper_id foreign key (paper_id) references papers (paper_id) on delete cascade on update cascade,
  primary key (question_id)
) default charset=utf8;

create table options (
  option_id int(11) unsigned not null auto_increment,
  option_name varchar(16) not null,
  content text,
  question_id int(11) unsigned not null,
  constraint options_question_id foreign key (question_id) references questions (question_id) on delete cascade on update cascade,
  primary key (option_id)
) default charset=utf8;

insert into users(username, password, email, admin) values('admin', '4da2379961eec3e436d7982310bd04df', 'admin@admin.com', 1);