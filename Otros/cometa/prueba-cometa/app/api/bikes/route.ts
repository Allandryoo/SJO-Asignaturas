import { db } from "@/src/db";
import { bikesTable } from "@/src/db/schema";
import { and, eq, lt } from "drizzle-orm";
import { NextResponse } from "next/server";

// Aplicar lazy expiration: si una reserva expiró, actualizarla a AVAILABLE
async function applyLazyExpiration() {
  const now = new Date();
  await db
    .update(bikesTable)
    .set({
      status: "AVAILABLE",
      reservedUntil: null,
      reservedBy: null,
      updatedAt: now,
    })
    .where(
      and(eq(bikesTable.status, "RESERVED"), lt(bikesTable.reservedUntil!, now))
    );
}

export async function GET() {
  try {
    await applyLazyExpiration();

    const bikes = await db.select().from(bikesTable);
    const bikesWithExpiration = bikes.map((bike) => {
      if (
        bike.status === "RESERVED" &&
        bike.reservedUntil &&
        bike.reservedUntil < new Date()
      ) {
        return {
          ...bike,
          status: "AVAILABLE" as const,
          reservedUntil: null,
          reservedBy: null,
        };
      }
      return bike;
    });
    return NextResponse.json({ bikes: bikesWithExpiration });
  } catch (error) {
    console.error("Error fetching bikes:", error);
    return NextResponse.json(
      { error: "Internal server error", message: "Failed to fetch bikes" },
      { status: 500 }
    );
  }
}
