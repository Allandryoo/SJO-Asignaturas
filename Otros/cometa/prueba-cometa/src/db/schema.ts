import { integer, pgTable, varchar, timestamp, pgEnum, index } from 'drizzle-orm/pg-core';

// Enum para estados de la moto
export const bikeStatusEnum = pgEnum('bike_status', ['AVAILABLE', 'RESERVED', 'IN_USE']);

export const bikesTable = pgTable('bikes', {
  id: integer().primaryKey().generatedAlwaysAsIdentity(),
  status: bikeStatusEnum('status').notNull().default('AVAILABLE'),
  reservedUntil: timestamp('reserved_until', { withTimezone: true }),
  reservedBy: varchar('reserved_by', { length: 255 }), // ID de usuario o email
  updatedAt: timestamp('updated_at', { withTimezone: true }).notNull().defaultNow(),
  rideStartedAt: timestamp('ride_started_at', { withTimezone: true }),
  latitude: varchar('latitude', { length: 50 }).notNull(),
  longitude: varchar('longitude', { length: 50 }).notNull(),
}, (table) => ({
  statusIdx: index('bikes_status_idx').on(table.status),
  reservedUntilIdx: index('bikes_reserved_until_idx').on(table.reservedUntil),
}));

// Tabla de usuarios (mantenida para referencia, puede ser útil más adelante)
export const usersTable = pgTable('users', {
  id: integer().primaryKey().generatedAlwaysAsIdentity(),
  name: varchar({ length: 255 }).notNull(),
  age: integer().notNull(),
  email: varchar({ length: 255 }).notNull().unique(),
});

