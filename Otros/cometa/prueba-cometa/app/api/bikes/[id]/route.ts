import { NextResponse } from 'next/server';
import { db } from '@/src/db';
import { bikesTable } from '@/src/db/schema';
import { eq } from 'drizzle-orm';

export async function GET(
  request: Request,
  { params }: { params: Promise<{ id: string }> }
) {
  try {
    const { id } = await params;
    const bikeId = parseInt(id);

    if (isNaN(bikeId)) {
      return NextResponse.json(
        { error: 'Invalid bike ID', message: 'Bike ID must be a number' },
        { status: 400 }
      );
    }

    // Obtener la moto primero
    const bikes = await db
      .select()
      .from(bikesTable)
      .where(eq(bikesTable.id, bikeId));

    if (bikes.length === 0) {
      return NextResponse.json(
        { error: 'Bike not found', message: `No bike found with id ${bikeId}` },
        { status: 404 }
      );
    }

    const bike = bikes[0];

    // Aplicar lazy expiration: si la reserva expiró, actualizar en BD
    const now = new Date();
    if (
      bike.status === 'RESERVED' &&
      bike.reservedUntil &&
      bike.reservedUntil < now
    ) {
      const updatedBikes = await db
        .update(bikesTable)
        .set({
          status: 'AVAILABLE',
          reservedUntil: null,
          reservedBy: null,
          updatedAt: now,
        })
        .where(eq(bikesTable.id, bikeId))
        .returning();

      return NextResponse.json(updatedBikes[0]);
    }

    return NextResponse.json(bike);
  } catch (error) {
    console.error('Error fetching bike:', error);
    return NextResponse.json(
      { error: 'Internal server error', message: 'Failed to fetch bike' },
      { status: 500 }
    );
  }
}

