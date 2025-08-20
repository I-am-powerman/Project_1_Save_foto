create table
  "public"."table_image" (
    "id" serial not null,
    "name_image" VARCHAR(255) not null,
    "path" varchar(255) not null,
    constraint "table_image_pkey" primary key ("id")
  )