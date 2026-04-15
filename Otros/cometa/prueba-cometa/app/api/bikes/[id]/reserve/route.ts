import { NextResponse } from 'next/server';

export async function POST(
  request: Request,
  { params }: { params: Promise<{ id: string }> }
) {
  try {
    const { id } = await params;
    const bikeId = parseInt(id);

    return NextResponse.json({ message: 'Bike reserved successfully' });
  } catch (error) {
    console.error('Error reserving bike:', error);
    return NextResponse.json(
      { error: 'Internal server error', message: 'Failed to reserve bike' },
      { status: 500 }
    );
  }
}

