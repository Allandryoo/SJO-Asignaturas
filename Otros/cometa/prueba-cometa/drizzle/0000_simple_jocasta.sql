CREATE TYPE "public"."bike_status" AS ENUM('AVAILABLE', 'RESERVED', 'IN_USE');--> statement-breakpoint
CREATE TABLE "bikes" (
	"id" integer PRIMARY KEY GENERATED ALWAYS AS IDENTITY (sequence name "bikes_id_seq" INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START WITH 1 CACHE 1),
	"status" "bike_status" DEFAULT 'AVAILABLE' NOT NULL,
	"reserved_until" timestamp with time zone,
	"reserved_by" varchar(255),
	"updated_at" timestamp with time zone DEFAULT now() NOT NULL,
	"ride_started_at" timestamp with time zone,
	"latitude" varchar(50) NOT NULL,
	"longitude" varchar(50) NOT NULL
);
--> statement-breakpoint
CREATE TABLE "users" (
	"id" integer PRIMARY KEY GENERATED ALWAYS AS IDENTITY (sequence name "users_id_seq" INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START WITH 1 CACHE 1),
	"name" varchar(255) NOT NULL,
	"age" integer NOT NULL,
	"email" varchar(255) NOT NULL,
	CONSTRAINT "users_email_unique" UNIQUE("email")
);
--> statement-breakpoint
CREATE INDEX "bikes_status_idx" ON "bikes" USING btree ("status");--> statement-breakpoint
CREATE INDEX "bikes_reserved_until_idx" ON "bikes" USING btree ("reserved_until");