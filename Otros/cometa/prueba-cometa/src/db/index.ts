import { drizzle } from 'drizzle-orm/postgres-js';
import postgres from 'postgres';

// Si usas el pool de conexiones de Supabase con modo "Transaction",
// es recomendable desactivar `prepare`, como sugiere la documentación.
const client = postgres(process.env.DATABASE_URL!, {
  prepare: false,
});

export const db = drizzle({ client });

